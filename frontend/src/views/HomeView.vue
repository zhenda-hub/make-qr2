<script setup>
import { ref } from 'vue'

const url = ref('')
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
  <div class="home">
    <!-- Hero Section -->
    <section class="hero">
      <div class="container">
        <h1>QR Studio</h1>
        <p class="subtitle">快速创建和管理您的二维码与网页</p>
        <div class="cta-buttons">
          <RouterLink to="/qr-generator" class="btn btn-primary">
            <i class="fas fa-qrcode"></i> 开始生成二维码
          </RouterLink>
          <RouterLink to="/page-manager" class="btn btn-secondary">
            <i class="fas fa-file-code"></i> 管理我的网页
          </RouterLink>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section class="features">
      <div class="container">
        <h2>主要功能</h2>
        <div class="feature-grid">
          <div class="feature-card">
            <div class="feature-icon">
              <i class="fas fa-qrcode"></i>
            </div>
            <h3>二维码生成</h3>
            <p>快速将网址转换为二维码，支持自定义颜色和尺寸</p>
          </div>

          <div class="feature-card">
            <div class="feature-icon">
              <i class="fas fa-file-code"></i>
            </div>
            <h3>网页管理</h3>
            <p>创建和编辑您的自定义网页，轻松管理内容</p>
          </div>

          <div class="feature-card">
            <div class="feature-icon">
              <i class="fas fa-mobile-alt"></i>
            </div>
            <h3>移动端预览</h3>
            <p>实时查看网页在移动设备上的显示效果</p>
          </div>

          <div class="feature-card">
            <div class="feature-icon">
              <i class="fas fa-cloud-download-alt"></i>
            </div>
            <h3>一键下载</h3>
            <p>轻松下载生成的二维码图片</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Quick QR Generator -->
    <section class="quick-generator">
      <div class="container">
        <h2>快速生成二维码</h2>
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

              <button @click="generateQR" class="btn btn-primary">
                <i class="fas fa-bolt"></i> 生成二维码
              </button>
            </div>

            <div class="qr-preview">
              <h3>二维码预览</h3>
              <div id="qrcode" ref="qrCode"></div>
              <button @click="downloadQR" class="btn btn-success">
                <i class="fas fa-download"></i> 下载PNG
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.home {
  padding-bottom: 60px;
}

.hero {
  text-align: center;
  padding: 80px 0;
  background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
  color: white;
  margin-bottom: 60px;
}

.hero h1 {
  font-size: 3.5rem;
  margin-bottom: 20px;
}

.hero .subtitle {
  font-size: 1.5rem;
  max-width: 700px;
  margin: 0 auto 40px;
  opacity: 0.9;
}

.cta-buttons {
  display: flex;
  gap: 20px;
  justify-content: center;
}

.features {
  padding: 60px 0;
  text-align: center;
}

.features h2 {
  font-size: 2.5rem;
  color: var(--primary);
  margin-bottom: 60px;
}

.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 30px;
  max-width: 1200px;
  margin: 0 auto;
}

.feature-card {
  background: white;
  border-radius: 12px;
  padding: 30px;
  box-shadow: var(--shadow);
  transition: transform 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-10px);
}

.feature-icon {
  width: 80px;
  height: 80px;
  background: rgba(67, 97, 238, 0.1);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 25px;
  color: var(--primary);
  font-size: 2rem;
}

.feature-card h3 {
  font-size: 1.5rem;
  margin-bottom: 15px;
  color: var(--dark);
}

.feature-card p {
  color: var(--gray);
  line-height: 1.6;
}

.quick-generator {
  padding: 60px 0;
  text-align: center;
}

.quick-generator h2 {
  font-size: 2.5rem;
  color: var(--primary);
  margin-bottom: 40px;
}

.qr-generator {
  display: flex;
  gap: 40px;
  flex-wrap: wrap;
  justify-content: center;
}

.qr-controls {
  flex: 1;
  min-width: 300px;
  max-width: 500px;
}

.qr-preview {
  flex: 1;
  min-width: 300px;
  max-width: 400px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

#qrcode {
  width: 250px;
  height: 250px;
  background: white;
  padding: 20px;
  border-radius: 12px;
  box-shadow: var(--shadow);
  margin: 20px 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

@media (max-width: 768px) {
  .hero h1 {
    font-size: 2.5rem;
  }

  .hero .subtitle {
    font-size: 1.2rem;
  }

  .cta-buttons {
    flex-direction: column;
    align-items: center;
  }

  .qr-generator {
    flex-direction: column;
  }
}
</style>
