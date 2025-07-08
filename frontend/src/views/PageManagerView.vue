<script setup>
import { ref, computed } from 'vue'

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

const savePage = () => {
  // Save logic will be implemented here
}

const generatePageQR = () => {
  // QR generation logic will be implemented here
}
</script>

<template>
  <div class="page-manager-view">
    <div class="page-title">
      <h1>网页管理</h1>
      <p>创建、编辑和管理您的自定义网页内容</p>
    </div>

    <div class="card">
      <div class="card-header">
        <h2>{{ currentPage?.title }}</h2>
        <div style="display: flex; gap: 10px;">
          <button @click="savePage" class="btn btn-success">
            <i class="fas fa-save"></i> 保存
          </button>
          <button @click="generatePageQR" class="btn btn-secondary">
            <i class="fas fa-qrcode"></i> 生成二维码
          </button>
        </div>
      </div>

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
  </div>
</template>

<style scoped>
.page-manager-view {
  padding: 20px;
}

.page-title {
  text-align: center;
  margin: 40px 0 30px;
  position: relative;
}

.page-title h1 {
  font-size: 2.5rem;
  color: #4361ee;
  margin-bottom: 15px;
}

.page-title p {
  font-size: 1.2rem;
  color: #6c757d;
  max-width: 700px;
  margin: 0 auto;
}

.page-title::after {
  content: '';
  display: block;
  width: 80px;
  height: 4px;
  background: #4cc9f0;
  margin: 20px auto 0;
  border-radius: 2px;
}

.card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 25px;
  margin-bottom: 30px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 1px solid #dee2e6;
}

.card-header h2 {
  font-size: 1.5rem;
  color: #4361ee;
}

.page-manager {
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 30px;
}

.page-list {
  background: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  max-height: 600px;
  overflow-y: auto;
}

.page-item {
  padding: 15px;
  margin-bottom: 10px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 1px solid #dee2e6;
}

.page-item:hover {
  background: #f1f3ff;
  border-color: #4361ee;
}

.page-item.active {
  background: #e6f0ff;
  border-color: #4361ee;
}

.page-item h3 {
  font-size: 1.2rem;
  margin-bottom: 5px;
}

.page-item .meta {
  display: flex;
  justify-content: space-between;
  color: #6c757d;
  font-size: 0.9rem;
}

.page-editor {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 25px;
}

.editor-area {
  background: white;
  border-radius: 12px;
  padding: 25px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.preview-area {
  background: white;
  border-radius: 12px;
  padding: 25px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.preview-phone {
  width: 280px;
  height: 500px;
  background: #f0f0f0;
  border-radius: 30px;
  padding: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  position: relative;
  overflow-y: auto;
}

.preview-phone:before {
  content: '';
  position: absolute;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  width: 40%;
  height: 6px;
  background: #ccc;
  border-radius: 3px;
}

.block-item {
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 8px;
  background: #f8f9fa;
  border: 1px solid #dee2e6;
}

.block-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.block-actions {
  display: flex;
  gap: 8px;
}

.block-content {
  padding: 10px 0;
}

.text-block {
  min-height: 100px;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 15px;
}

.image-block {
  min-height: 150px;
  background: #f0f0f0;
  border: 2px dashed #dee2e6;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #6c757d;
}

.video-block {
  min-height: 150px;
  background: #f0f0f0;
  border: 2px dashed #dee2e6;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #6c757d;
}

.block-controls {
  display: flex;
  gap: 15px;
  margin-top: 20px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  color: #212529;
}

.form-control {
  width: 100%;
  padding: 14px;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  font-size: 1rem;
  transition: border 0.3s ease;
}

.form-control:focus {
  outline: none;
  border-color: #4361ee;
  box-shadow: 0 0 0 3px rgba(67, 97, 238, 0.2);
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  text-decoration: none;
}

.btn-primary {
  background: #4361ee;
  color: white;
}

.btn-primary:hover {
  background: #3f37c9;
}

.btn-secondary {
  background: #f8f9fa;
  color: #212529;
  border: 1px solid #dee2e6;
}

.btn-secondary:hover {
  background: #e9ecef;
}

.btn-success {
  background: #4ade80;
  color: white;
}

.btn-danger {
  background: #f87171;
  color: white;
}

.btn-sm {
  padding: 8px 16px;
  font-size: 0.9rem;
}

/* 移动端优化 */
@media (max-width: 576px) {
  .page-title h1 {
    font-size: 1.8rem;
  }

  .page-title p {
    font-size: 1rem;
  }

  .card-header {
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
  }

  .page-item {
    padding: 12px;
  }

  .block-item {
    padding: 12px;
  }

  .preview-phone {
    width: 100%;
    height: 400px;
    border-radius: 12px;
  }

  .btn {
    padding: 10px 15px;
    font-size: 0.9rem;
  }
}

.page-manager {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.page-editor {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

@media (min-width: 992px) {
  .page-manager {
    display: grid;
    grid-template-columns: 300px 1fr;
    gap: 30px;
  }

  .page-editor {
    display: grid;
    grid-template-columns: 1fr 300px;
    gap: 25px;
  }
}

@media (max-width: 768px) {
  .page-list {
    max-height: none;
  }
}
</style>
