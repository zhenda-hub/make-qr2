<script setup>
import { ref } from 'vue'

// QR Generator state
const url = ref('https://www.example.com/product-page')
const size = ref('200')
const fgColor = ref('#000000')
const bgColor = ref('#ffffff')
const qrCode = ref(null)

const generateQR = () => {
  if (!url.value) return
  // QR generation logic will be implemented here
}

const downloadQR = () => {
  // QR download logic will be implemented here
}
</script>

<template>
  <div class="qr-generator-view">
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
  </div>
</template>

<style scoped>
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
