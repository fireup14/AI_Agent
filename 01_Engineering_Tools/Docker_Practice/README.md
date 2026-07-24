# Docker 容器化实践库

本文件夹包含一个极简的 Python 应用和一个 `Dockerfile`，供你进行容器化实战。

## 🛠️ 推荐练习步骤

确保你的系统上已经安装并启动了 Docker 引擎。

1. **构建镜像**：
   在 `Docker_Practice` 目录下打开终端，执行以下命令构建名为 `my-python-app` 的镜像（注意末尾有一个 `.`）：
   ```bash
   docker build -t my-python-app .
   ```
2. **查看本地镜像**：
   ```bash
   docker images
   ```
3. **运行容器**：
   使用刚刚构建的镜像启动一个容器：
   ```bash
   docker run --name test-container my-python-app
   ```
   你应该能看到容器内控制台打印出的循环日志。
4. **清理容器**：
   - 查看运行过或退出的容器：`docker ps -a`
   - 删除容器：`docker rm test-container`
   - 删除镜像：`docker rmi my-python-app`
