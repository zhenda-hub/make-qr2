<script setup>
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const activeTab = computed(() => route.name)

// QR Generator state
const url = ref('https://www.example.com/product-page')
const size = ref('200')
const fgColor = ref('#000000')
const bgColor = ref('#ffffff')
const qrCode = ref(null)

// Page Manager state
const pages = ref([
  { id: 1, title: '产品介绍页', modified: '今天 14:30', blocks: 3, active: true },
  { id: 2, title: '活动宣传页', modified: '昨天 10:15', blocks: 5, active: false },
  { id: 3, title: '公司简介', modified: '2023-07-25', blocks: 4, active: false },
  { id: 4, title: '服务价格表', modified: '2023-07-20', blocks: 2, active: false }
])

const currentPage = computed(() => pages.value.find(p => p.active))
const blocks = ref([
  { id: 1, type: 'text', content: '欢迎使用我们的产品\n这是一款改变您工作方式的革命性产品，具有卓越性能和易用性。' },
  { id: 2, type: 'image', content: '产品主图.jpg' },
  { id: 3, type: 'video', content: '产品演示视频' }
])

const generateQR = () => {
  if (!url.value) return
  // QR generation logic will be implemented here
}

const downloadQR = () => {
  // QR download logic will be implemented here
}
</script>

<template>
  <div class="advanced-view">
    <!-- QR Generator Section -->
    <section v-if="activeTab === 'qr-generator'" id="qr-generator">
      <div class="page-title">
        <h1>二维码生成器</h1>
        <p>将您的网址转换为二维码图片，支持自定义颜色和尺寸</p>
      </div>

      <div class="card">
        <div class="qr-generator">
          <div class="qr-controls">
            <div class="form-group">
              <label for="url-input">输入网址</label>
              <input
                v-model="url"
                type="url"
                id="url-input"
                class="form-control"
                placeholder="https://example.com"
              >
            </div>

            <div class="form-group">
              <label>二维码尺寸</label>
              <div style="display: flex; gap: 15px;">
                <label style="flex: 1;">
                  <input type="radio" v-model="size" value="200"> 小 (200×200)
                </label>
                <label style="flex: 1;">
                  <input type="radio" v-model="size" value="300"> 中 (300×300)
                </label>
                <label style="flex: 1;">
                  <input type="radio" v-model="size" value="400"> 大 (400×400)
                </label>
              </div>
            </div>

            <div class="form-group">
              <label for="foreground-color">前景色</label>
              <input type="color" v-model="fgColor" id="foreground-color" class="form-control">
            </div>

            <div class="form-group">
              <label for="background-color">背景色</label>
              <input type="color" v-model="bgColor" id="background-color" class="form-control">
            </div>

            <button @click="generateQR" class="btn btn-primary" style="width: 100%;">
              <i class="fas fa-bolt"></i> 生成二维码
            </button>
          </div>

          <div class="qr-preview">
            <h3>二维码预览</h3>
            <div id="qrcode" ref="qrCode"></div>
            <div style="display: flex; gap: 15px; margin-top: 20px;">
              <button @click="downloadQR" class="btn btn-success">
                <i class="fas fa-download"></i> 下载PNG
              </button>
              <button class="btn btn-secondary">
                <i class="fas fa-copy"></i> 复制图片
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Page Manager Section -->
    <section v-if="activeTab === 'page-manager'" id="page-manager">
      <div class="page-title">
        <h1>网页管理</h1>
        <p>创建、编辑和管理您的自定义网页内容</p>
      </div>

      <div class="card">
        <div class="page-manager">
          <div class="page-list">
            <div style="display: flex; margin-bottom: 15px; gap: 10px;">
              <input type="text" class="form-control" placeholder="搜索网页...">
              <button class="btn btn-primary">
                <i class="fas fa-search"></i>
              </button>
            </div>

            <button class="btn btn-primary" style="width: 100%; margin-bottom: 20px;">
              <i class="fas fa-plus"></i> 新建网页
            </button>

            <div
              v-for="page in pages"
              :key="page.id"
              class="page-item"
              :class="{ active: page.active }"
              @click="pages.forEach(p => p.active = p.id === page.id)"
            >
              <h3>{{ page.title }}</h3>
              <div class="meta">
                <span>修改: {{ page.modified }}</span>
                <span>{{ page.blocks }}个内容块</span>
              </div>
            </div>
          </div>

          <div class="page-editor">
            <div class="editor-area">
              <div class="form-group">
                <label for="page-title">网页标题</label>
                <input
                  v-model="currentPage.title"
                  type="text"
                  id="page-title"
                  class="form-control"
                >
              </div>

              <h3 style="margin: 25px 0 15px;">内容块</h3>

              <div
                v-for="block in blocks"
                :key="block.id"
                class="block-item"
              >
                <div class="block-header">
                  <h4>
                    <i
                      :class="{
                        'fas fa-heading': block.type === 'text',
                        'fas fa-image': block.type === 'image',
                        'fas fa-video': block.type === 'video'
                      }"
                    ></i>
                    {{
                      block.type === 'text' ? '标题文本' :
                      block.type === 'image' ? '产品图片' : '产品视频'
                    }}
                  </h4>
                  <div class="block-actions">
                    <button class="btn btn-sm btn-secondary">
                      <i class="fas fa-arrow-up"></i>
                    </button>
                    <button class="btn btn-sm btn-secondary">
                      <i class="fas fa-arrow-down"></i>
                    </button>
                    <button class="btn btn-sm btn-danger">
                      <i class="fas fa-trash"></i>
                    </button>
                  </div>
                </div>
                <div class="block-content">
                  <div
                    :class="{
                      'text-block': block.type === 'text',
                      'image-block': block.type === 'image',
                      'video-block': block.type === 'video'
                    }"
                  >
                    {{ block.content }}
                  </div>
                </div>
              </div>

              <div class="block-controls">
                <button class="btn btn-secondary">
                  <i class="fas fa-plus"></i> 添加文本块
                </button>
                <button class="btn btn-secondary">
                  <i class="fas fa-plus"></i> 添加图片块
                </button>
                <button class="btn btn-secondary">
                  <i class="fas fa-plus"></i> 添加视频块
                </button>
              </div>
            </div>

            <div class="preview-area">
              <h3>移动端预览</h3>
              <div class="preview-phone">
                <h2 style="text-align: center; margin: 20px 0;">{{ currentPage?.title }}</h2>
                <div
                  v-for="block in blocks"
                  :key="block.id"
                  style="background: white; padding: 20px; border-radius: 10px; margin-bottom: 15px;"
                >
                  <template v-if="block.type === 'text'">
                    <div v-html="block.content.replace('\n', '<br>')"></div>
                  </template>
                  <template v-else>
                    <div style="height: 200px; display: flex; align-items: center; justify-content: center;">
                      <i
                        :class="{
                          'fas fa-image fa-3x': block.type === 'image',
                          'fas fa-video fa-3x': block.type === 'video'
                        }"
                      ></i>
                    </div>
                  </template>
                </div>
              </div>

              <div style="margin-top: 20px; text-align: center;">
                <h3>此页面的二维码</h3>
                <div style="width: 150px; height: 150px; background: #eee; margin: 10px auto; display: flex; align-items: center; justify-content: center;">
                  <i class="fas fa-qrcode fa-3x"></i>
                </div>
                <button class="btn btn-sm btn-success">
                  <i class="fas fa-download"></i> 下载二维码
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* Styles remain the same as previous version */
</style>
