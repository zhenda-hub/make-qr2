<script setup>
import { ref, nextTick } from 'vue'

// QR Generator state
const url = ref('https://www.baidu.com/')
const size = ref('200')
const fgColor = ref('#000000')
const bgColor = ref('#ffffff')
const qrCode = ref(null)
const isLoading = ref(false)
const error = ref(null)
const qrImageUrl = ref('')

    const generateQR = async () => {
      if (!url.value) {
        error.value = '请输入有效的URL'
        return
      }

      try {
        isLoading.value = true
        error.value = null
        qrImageUrl.value = ''

        // Force re-render of img element
        await nextTick()

        const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8003'
        
        // Prepare request data
        const requestData = {
          url: url.value,
          size: parseInt(size.value),
          fg_color: fgColor.value,
          bg_color: bgColor.value
        }

        // Make POST request to the API
        const response = await fetch(`${apiUrl}/api/qrcode`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(requestData)
        })

        if (!response.ok) {
          const errorData = await response.json().catch(() => ({}))
          throw new Error(errorData.detail || '请求失败')
        }

        const data = await response.json()
        
        if (!data.image_url) {
          throw new Error('无效的响应格式')
        }

        // Add base URL and timestamp to prevent caching
        const baseUrl = import.meta.env.VITE_API_URL || 'http://localhost:8003'
        // Ensure the image_url doesn't already have the base URL
        const imagePath = data.image_url.startsWith('http') ? data.image_url : `${baseUrl}${data.image_url}`
        qrImageUrl.value = `${imagePath}?t=${Date.now()}`
        console.log('QR code generated:', qrImageUrl.value)
      } catch (err) {
        console.error('Error generating QR code:', err)
        error.value = `生成二维码失败: ${err.message || '未知错误'}`
      } finally {
        isLoading.value = false
      }
    }

const downloadQR = async () => {
  if (!qrImageUrl.value) {
    error.value = '请先生成二维码'
    return
  }

  try {
    const response = await fetch(qrImageUrl.value)
    if (!response.ok) throw new Error('下载失败')

    const blob = await response.blob()
    const url = window.URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.download = `qrcode-${new Date().getTime()}.png`
    document.body.appendChild(link)
    link.click()
    window.URL.revokeObjectURL(url)
    document.body.removeChild(link)
  } catch (err) {
    error.value = '下载失败: ' + err.message
  }
}
</script>

<template>
  <div class="qr-generator-view">
    <div class="page-title">
      <h1>二维码生成器</h1>
      <p>将您的网址转换为二维码图片，支持自定义颜色和尺寸</p>
    </div>
    
    <!-- Error Message -->
    <div v-if="error" class="error-message">
      {{ error }}
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
            <div class="size-options">
              <label>
                <input type="radio" v-model="size" value="200"> 小 (200×200)
              </label>
              <label>
                <input type="radio" v-model="size" value="300"> 中 (300×300)
              </label>
              <label>
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

          <div class="form-actions">
            <button @click="generateQR" class="btn btn-primary" :disabled="isLoading">
              <span v-if="isLoading">生成中...</span>
              <span v-else>生成二维码</span>
            </button>
            <button 
              v-if="qrImageUrl" 
              @click="downloadQR" 
              class="btn btn-secondary"
              :disabled="isLoading"
            >
              下载二维码
            </button>
          </div>
        </div> <!-- 关闭 qr-controls div -->

        <div class="qr-preview">
          <h3>二维码预览</h3>
          <div id="qrcode" ref="qrCode">
            <template v-if="isLoading">
              <div class="loading-spinner">
                <i class="fas fa-spinner fa-spin"></i> 正在生成二维码...
              </div>
            </template>
            <template v-else-if="qrImageUrl">
              <img :src="qrImageUrl" alt="生成的二维码" style="max-width: 100%; height: auto;">
            </template>
            <template v-else>
              <div class="placeholder">
                <i class="fas fa-qrcode"></i> 二维码将在这里显示
              </div>
            </template>
          </div>
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
  </div>
</template>

<style scoped>
/* Base styles */
:root {
  --primary-color: #4a6cf7;
  --primary-hover: #3a5ce4;
  --secondary-color: #6c757d;
  --success-color: #28a745;
  --danger-color: #dc3545;
  --light-gray: #f8f9fa;
  --border-color: #dee2e6;
  --border-radius: 8px;
  --box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  --transition: all 0.3s ease;
}

/* Reset and base styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f5f7ff;
}

/* Layout */
.qr-generator-view {
  max-width: 1000px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

.page-title {
  text-align: center;
  margin-bottom: 2rem;
}

.page-title h1 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
  font-size: 2.2rem;
}

.page-title p {
  color: #7f8c8d;
  font-size: 1.1rem;
}

/* Card */
.card {
  background: white;
  border-radius: var(--border-radius);
  box-shadow: var(--box-shadow);
  padding: 2rem;
  margin-bottom: 2rem;
}

/* Form styles */
.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: #495057;
}

.form-control {
  width: 100%;
  padding: 0.75rem 1rem;
  font-size: 1rem;
  border: 1px solid var(--border-color);
  border-radius: var(--border-radius);
  transition: var(--transition);
}

.form-control:focus {
  border-color: var(--primary-color);
  box-shadow: 0 0 0 0.2rem rgba(74, 108, 247, 0.25);
  outline: none;
}

/* Size options */
.size-options {
  display: flex;
  gap: 1rem;
  margin-top: 0.5rem;
}

.size-options label {
  flex: 1;
  display: flex;
  align-items: center;
  padding: 0.75rem;
  background: var(--light-gray);
  border-radius: var(--border-radius);
  cursor: pointer;
  transition: var(--transition);
  border: 1px solid transparent;
}

.size-options label:hover {
  border-color: var(--primary-color);
}

.size-options input[type="radio"] {
  margin-right: 0.5rem;
}

/* Color inputs */
.color-inputs {
  display: flex;
  gap: 1rem;
}

.color-input {
  flex: 1;
}

.color-input input[type="color"] {
  width: 100%;
  height: 45px;
  padding: 0;
  border: 1px solid var(--border-color);
  border-radius: var(--border-radius);
  cursor: pointer;
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  font-weight: 500;
  border: none;
  border-radius: var(--border-radius);
  cursor: pointer;
  transition: var(--transition);
  text-decoration: none;
  gap: 0.5rem;
}

.btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.btn-primary {
  background-color: var(--primary-color);
  color: white;
}

.btn-primary:hover:not(:disabled) {
  background-color: var(--primary-hover);
  transform: translateY(-1px);
}

.btn-secondary {
  background-color: var(--secondary-color);
  color: white;
}

.btn-secondary:hover:not(:disabled) {
  background-color: #5a6268;
  transform: translateY(-1px);
}

/* Form actions */
.form-actions {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
}

/* QR Preview */
.qr-preview {
  margin-top: 2rem;
  text-align: center;
  padding: 2rem;
  background: var(--light-gray);
  border-radius: var(--border-radius);
  transition: var(--transition);
}

.qr-preview h3 {
  margin-bottom: 1rem;
  color: #2c3e50;
}

.qr-image-container {
  max-width: 300px;
  margin: 0 auto;
  padding: 1rem;
  background: white;
  border-radius: var(--border-radius);
  box-shadow: var(--box-shadow);
}

.qr-image {
  width: 100%;
  height: auto;
  border-radius: 4px;
  transition: var(--transition);
}

.qr-image:hover {
  transform: scale(1.03);
}

/* Error message */
.error-message {
  background-color: #ffebee;
  color: #c62828;
  padding: 1rem;
  border-radius: var(--border-radius);
  margin-bottom: 1.5rem;
  border-left: 4px solid #ef5350;
  animation: fadeIn 0.3s ease;
}

/* Loading state */
@keyframes spin {
  to { transform: rotate(360deg); }
}

.loading-spinner {
  display: inline-block;
  width: 1.25rem;
  height: 1.25rem;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  border-top-color: white;
  animation: spin 0.8s ease-in-out infinite;
  margin-right: 0.5rem;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .size-options {
    flex-direction: column;
  }
  
  .form-actions {
    flex-direction: column;
  }
  
  .btn {
    width: 100%;
  }
  
  .color-inputs {
    flex-direction: column;
  }
}

/* Animations */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
.error-message {
  background-color: #ffebee;
  color: #c62828;
  padding: 12px 16px;
  border-radius: 4px;
  margin-bottom: 20px;
  border-left: 4px solid #ef5350;
}

.qr-preview {
  text-align: center;
  margin: 20px 0;
  padding: 20px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.qr-image {
  max-width: 100%;
  height: auto;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  transition: transform 0.3s ease;
}

.qr-image:hover {
  transform: scale(1.02);
}

.qr-generator-view {
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

.qr-generator {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.qr-controls {
  width: 100%;
}

.qr-preview {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

@media (min-width: 768px) {
  .qr-generator {
    flex-direction: row;
    gap: 40px;
  }

  .qr-controls {
    flex: 1;
    min-width: 300px;
  }

  .qr-preview {
    flex: 1;
    min-width: 300px;
  }
}

#qrcode {
  width: 250px;
  height: 250px;
  background: white;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  margin: 20px 0;
  display: flex;
  align-items: center;
  justify-content: center;
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

  .form-control {
    padding: 12px;
  }

  .btn {
    padding: 10px 20px;
  }

  #qrcode {
    width: 200px;
    height: 200px;
  }
}
</style>
