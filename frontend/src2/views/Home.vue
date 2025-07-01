<template>
  <div class="home">
    <!-- 顶部横幅 -->
    <div class="hero-section">
      <el-row :gutter="20" justify="center" align="middle">
        <el-col :xs="24" :sm="24" :md="12">
          <h1 class="hero-title">欢迎使用 Web Demo</h1>
          <p class="hero-subtitle">一个使用 Vue 3 + FastAPI 构建的现代化应用</p>
          <el-space>
            <el-button type="primary" size="large">开始使用</el-button>
            <el-button size="large">了解更多</el-button>
          </el-space>
        </el-col>
        <el-col :xs="24" :sm="24" :md="12" class="hero-image">
          <img src="https://placeholder.co/600x400" alt="Hero Image">
        </el-col>
      </el-row>
    </div>

    <!-- 功能特点 -->
    <div class="features-section">
      <h2 class="section-title">主要功能</h2>
      <el-row :gutter="20">
        <el-col :xs="24" :sm="12" :md="8">
          <el-card class="feature-card">
            <template #header>
              <div class="card-header">
                <el-icon><Monitor /></el-icon>
                <span>响应式设计</span>
              </div>
            </template>
            <p>完美适配各种设备尺寸，提供最佳用户体验</p>
          </el-card>
        </el-col>
        <el-col :xs="24" :sm="12" :md="8">
          <el-card class="feature-card">
            <template #header>
              <div class="card-header">
                <el-icon><Connection /></el-icon>
                <span>API 集成</span>
              </div>
            </template>
            <p>强大的 FastAPI 后端支持，实现高效数据交互</p>
          </el-card>
        </el-col>
        <el-col :xs="24" :sm="12" :md="8">
          <el-card class="feature-card">
            <template #header>
              <div class="card-header">
                <el-icon><Lock /></el-icon>
                <span>安全可靠</span>
              </div>
            </template>
            <p>内置安全机制，保护您的数据安全</p>
          </el-card>
        </el-col>
      </el-row>
    </div>

    <!-- 最新动态 -->
    <div class="news-section">
      <h2 class="section-title">最新动态</h2>
      <el-timeline>
        <el-timeline-item
          v-for="(activity, index) in activities"
          :key="index"
          :timestamp="activity.timestamp"
          :type="activity.type"
        >
          {{ activity.content }}
        </el-timeline-item>
      </el-timeline>
    </div>
  </div>
</template>

<script setup>
import { Monitor, Connection, Lock } from '@element-plus/icons-vue'

const activities = [
  {
    content: '项目正式发布',
    timestamp: '2025-02-24',
    type: 'success'
  },
  {
    content: '添加新功能',
    timestamp: '2025-02-23',
    type: 'info'
  },
  {
    content: '修复已知问题',
    timestamp: '2025-02-22',
    type: 'warning'
  }
]
</script>

<style scoped>
.home {
  max-width: 1200px;
  margin: 0 auto;
}

/* 英雄区样式 */
.hero-section {
  padding: 40px 20px;
  margin-bottom: 40px;
  background: linear-gradient(135deg, var(--el-color-primary-light-8) 0%, #fff 100%);
  border-radius: 8px;
}

.hero-title {
  font-size: 2.5rem;
  color: var(--el-color-primary);
  margin-bottom: 20px;
}

.hero-subtitle {
  font-size: 1.2rem;
  color: var(--el-text-color-secondary);
  margin-bottom: 30px;
}

.hero-image img {
  width: 100%;
  max-width: 600px;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

/* 功能区样式 */
.features-section {
  padding: 40px 20px;
  margin-bottom: 40px;
}

.section-title {
  text-align: center;
  margin-bottom: 40px;
  color: var(--el-text-color-primary);
}

.feature-card {
  margin-bottom: 20px;
  transition: transform 0.3s;
}

.feature-card:hover {
  transform: translateY(-5px);
}

.card-header {
  display: flex;
  align-items: center;
  gap: 10px;
}

.card-header .el-icon {
  font-size: 24px;
  color: var(--el-color-primary);
}

/* 动态区样式 */
.news-section {
  padding: 40px 20px;
}

/* 响应式调整 */
@media screen and (max-width: 768px) {
  .hero-title {
    font-size: 2rem;
  }

  .hero-subtitle {
    font-size: 1rem;
  }

  .hero-image {
    margin-top: 20px;
  }

  .features-section,
  .news-section {
    padding: 20px 10px;
  }
}
</style>
