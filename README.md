# 多媒体二维码生成系统

基于Vue + FastAPI实现的二维码生成系统，支持批量上传图片/视频并生成可扫描查看的二维码。

## 功能特性

- 网址转二维码图片
- 自定义二维码尺寸和颜色
- 下载PNG格式二维码
- 批量处理功能

## 技术栈

- 前端：Vue 3 + Vite
- 后端：FastAPI
- 二维码生成：qrcode + pillow

## 快速开始

### 开发环境运行

```bash
# 启动后端服务
cd backend2
pip install -r requirements.txt
uvicorn app.main:app --reload

# 启动前端开发服务器
cd ../frontend
npm install
npm run dev
```

### Docker部署

```bash
docker compose up --build -d
```

## 使用说明

1. 访问前端页面：http://localhost:5174
2. 输入网址并点击"生成二维码"
3. 预览生成的二维码
4. 点击"下载二维码"保存图片

## 项目结构

```
├── backend2/          # FastAPI后端
├── frontend/          # Vue前端
├── docker-compose.yml # Docker配置
└── README.md          # 项目文档
```
