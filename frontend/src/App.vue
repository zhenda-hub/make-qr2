<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="container">
      <nav class="navbar">
        <RouterLink to="/" class="logo">
          <i class="fas fa-qrcode"></i>
          <span>QR Studio</span>
        </RouterLink>
        <div class="nav-links">
          <RouterLink to="/" class="active">
            <i class="fas fa-home"></i> 首页
          </RouterLink>
          <RouterLink to="/qr-generator">
            <i class="fas fa-qrcode"></i> 二维码生成
          </RouterLink>
          <RouterLink to="/page-manager">
            <i class="fas fa-file-code"></i> 网页管理
          </RouterLink>
        </div>
      </nav>
    </div>
  </header>

  <main class="container">
    <RouterView />
  </main>

  <footer>
    <div class="container">
      <p>© 2023 QR Studio - 二维码生成与网页管理平台 | 轻松创建自定义页面和二维码</p>
    </div>
  </footer>
</template>

<style>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

:root {
  --primary: #4361ee;
  --secondary: #3f37c9;
  --accent: #4cc9f0;
  --light: #f8f9fa;
  --dark: #212529;
  --success: #4ade80;
  --warning: #facc15;
  --danger: #f87171;
  --gray: #6c757d;
  --border: #dee2e6;
  --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

body {
  background: linear-gradient(135deg, #f5f7fa 0%, #e4edf5 100%);
  color: var(--dark);
  line-height: 1.6;
  min-height: 100vh;
}

.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 20px;
}

/* 导航栏样式 */
header {
  background: linear-gradient(to right, var(--primary), var(--secondary));
  color: white;
  box-shadow: var(--shadow);
  position: sticky;
  top: 0;
  z-index: 100;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 0;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 1.8rem;
  font-weight: 700;
  color: white;
  text-decoration: none;
}

.logo i {
  color: var(--accent);
}

.nav-links {
  display: flex;
  gap: 25px;
}

.nav-links a {
  color: rgba(255, 255, 255, 0.85);
  text-decoration: none;
  font-weight: 500;
  font-size: 1.1rem;
  transition: all 0.3s ease;
  padding: 8px 12px;
  border-radius: 5px;
}

.nav-links a:hover,
.nav-links a.active {
  background: rgba(255, 255, 255, 0.15);
  color: white;
}

footer {
  text-align: center;
  padding: 30px 0;
  color: var(--gray);
  margin-top: 40px;
}
</style>
