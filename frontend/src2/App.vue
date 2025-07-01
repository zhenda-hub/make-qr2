<template>
  <el-container class="layout-container">
    <!-- 顶部导航栏 -->
    <el-header class="header" height="60px">
      <div class="nav-container">
        <!-- Logo区域 -->
        <div class="logo-section">
          <h2 class="logo">Web Demo</h2>
        </div>
        
        <!-- 导航菜单 -->
        <el-menu
          :default-active="activeIndex"
          class="nav-menu"
          mode="horizontal"
          :ellipsis="false"
          @select="handleSelect"
        >
          <el-menu-item index="/">首页</el-menu-item>
          <el-menu-item index="/about">关于</el-menu-item>
          <el-sub-menu index="services">
            <template #title>服务</template>
            <el-menu-item index="/service1">服务1</el-menu-item>
            <el-menu-item index="/service2">服务2</el-menu-item>
          </el-sub-menu>
        </el-menu>

        <!-- 用户区域 -->
        <div class="user-section">
          <el-space>
            <el-button type="primary" plain>登录</el-button>
            <el-button type="success">注册</el-button>
          </el-space>
        </div>
      </div>
    </el-header>

    <!-- 主要内容区 -->
    <el-main class="main-content">
      <router-view></router-view>
    </el-main>

    <!-- 底部 -->
    <el-footer height="60px" class="footer">
      <p>&copy; 2025 Web Demo. All rights reserved.</p>
    </el-footer>
  </el-container>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const activeIndex = ref('/')

const handleSelect = (key) => {
  router.push(key)
}
</script>

<style scoped>
/* 布局容器 */
.layout-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* 顶部导航栏 */
.header {
  padding: 0;
  background-color: #fff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  position: fixed;
  width: 100%;
  z-index: 1000;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  height: 100%;
  padding: 0 20px;
}

/* Logo样式 */
.logo-section {
  margin-right: 40px;
}

.logo {
  margin: 0;
  font-size: 1.5rem;
  color: var(--el-color-primary);
}

/* 导航菜单 */
.nav-menu {
  flex-grow: 1;
  border-bottom: none;
}

/* 用户区域 */
.user-section {
  margin-left: auto;
}

/* 主内容区 */
.main-content {
  margin-top: 60px; /* 为固定的header留出空间 */
  padding: 20px;
  flex: 1;
  background-color: #f5f7fa;
}

/* 底部 */
.footer {
  text-align: center;
  background-color: #fff;
  color: #666;
  padding: 20px 0;
  border-top: 1px solid #eee;
}

/* 响应式设计 */
@media screen and (max-width: 768px) {
  .nav-container {
    padding: 0 10px;
  }

  .logo-section {
    margin-right: 20px;
  }

  .user-section {
    display: none; /* 在移动端隐藏按钮 */
  }

  .nav-menu {
    padding: 0 5px;
  }
}
</style>

<style>
/* 全局样式 */
body {
  margin: 0;
  padding: 0;
  font-family: var(--el-font-family);
}

/* 确保el-menu在移动端正确显示 */
.el-menu--popup {
  min-width: 200px;
}
</style>
