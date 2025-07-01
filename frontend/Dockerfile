# 使用 Node.js 作为基础镜像
FROM node:18-alpine
# FROM node:latest # 大小是alpine4倍

# 设置工作目录
WORKDIR /app

# # 复制 package.json 和 package-lock.json（如果存在）
COPY package*.json ./

# 安装依赖
RUN npm install

# 设置热更新的环境变量
ENV CHOKIDAR_USEPOLLING=true
ENV WATCHPACK_POLLING=true

# 默认命令
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
