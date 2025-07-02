<script setup>
import { ref } from 'vue'
import axios from 'axios'

const url = ref('')
const qrImage = ref(null)
const isLoading = ref(false)

const generateQR = async () => {
  if (!url.value) return

  isLoading.value = true
  try {
    const response = await axios.get('http://localhost:8003/api/qrcode', {
      params: { url: url.value },
      responseType: 'blob'
    })
    qrImage.value = URL.createObjectURL(response.data)
  } catch (error) {
    console.error('生成二维码失败:', error)
    alert('生成二维码失败，请检查网址格式')
  } finally {
    isLoading.value = false
  }
}

const downloadQR = () => {
  if (qrImage.value) {
    const link = document.createElement('a')
    link.href = qrImage.value
    link.download = `qrcode_${new Date().getTime()}.png`
    link.click()
  }
}
</script>

<template>
  <div class="container">
    <el-row :gutter="20" justify="center">
      <el-col :xs="24" :sm="20" :md="16" :lg="12">
        <el-card shadow="hover">
          <template #header>
            <div class="card-header">
              <h1>多媒体二维码生成器</h1>
              <p>输入网址生成可扫描的二维码</p>
            </div>
          </template>

          <el-form @submit.prevent="generateQR">
            <el-form-item>
              <el-input
                v-model="url"
                placeholder="https://example.com"
                type="url"
                clearable
                @keyup.enter="generateQR"
              />
            </el-form-item>
            <el-form-item>
              <el-button
                type="primary"
                :loading="isLoading"
                :disabled="!url"
                @click="generateQR"
              >
                生成二维码
              </el-button>
            </el-form-item>
          </el-form>

          <div v-if="qrImage" class="result-section">
            <el-image :src="qrImage" class="qr-image" fit="contain" />
            <el-button
              type="success"
              class="download-btn"
              @click="downloadQR"
            >
              下载二维码
            </el-button>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<style scoped>
.container {
  padding: 20px;
}

.card-header {
  text-align: center;
}

.card-header h1 {
  color: var(--el-color-primary);
  margin-bottom: 8px;
}

.card-header p {
  color: var(--el-text-color-secondary);
}

.result-section {
  margin-top: 20px;
  text-align: center;
}

.qr-image {
  width: 200px;
  height: 200px;
  margin-bottom: 16px;
  background: #f5f7fa;
  padding: 10px;
  border-radius: 4px;
}

.download-btn {
  margin-top: 10px;
}
</style>
