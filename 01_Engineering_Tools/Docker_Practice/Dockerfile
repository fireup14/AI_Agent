# Docker_Practice/Dockerfile
# 基础镜像使用轻量级的 python:3.10-slim
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 将当前目录下的文件复制到工作目录中
COPY . /app

# 容器启动时运行的默认命令
CMD ["python", "app.py"]
