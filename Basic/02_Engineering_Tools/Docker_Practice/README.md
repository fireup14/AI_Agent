# Docker 一日学习计划

> 适合人群：具备 Linux 常用命令、Git 和 Python 基础，希望在一天内建立 Docker 的完整入门认知并完成一次容器化实践。

## 一、今天要达到的结果

完成约 8 小时学习后，你应该能够：

- [ ] 用自己的话解释镜像、容器、仓库、Dockerfile、数据卷和网络
- [ ] 独立完成容器的查看、启动、停止、删除和日志排查
- [ ] 为本目录的 Python 程序构建镜像并运行容器
- [ ] 使用端口映射、绑定挂载和自定义网络
- [ ] 使用 Docker Compose 管理一个简单服务
- [ ] 根据日志和容器状态排查常见问题
- [ ] 将当天的学习记录和代码通过 Git 提交

今天不追求 Kubernetes、复杂镜像优化、生产环境安全和 CI/CD。一天的目标是先打通完整工作流，而不是记住所有命令。

## 二、开始前的准备（09:00—09:30）

### 目标

确认 Docker 引擎可以正常工作，并理解 Docker 在当前系统中的运行位置。

### 任务

在 PowerShell 中进入本目录，然后执行：

```powershell
cd E:\HelloWorld\AI_Agent\01_Engineering_Tools\Docker_Practice
docker version
docker info
docker run --rm hello-world
```

重点观察：

- `docker version` 中 Client 与 Server 的区别
- `docker info` 中容器数、镜像数和 Docker Root Dir
- `--rm` 表示容器退出后自动删除

### 产出与验收

- [ ] `hello-world` 能够正常运行
- [ ] 能说明 Docker CLI 与 Docker Engine 不是同一个组件
- [ ] 若执行失败，已记录完整错误信息，而不是反复重装

## 三、模块 1：核心概念与生命周期（09:30—10:30）

### 目标

建立“镜像是模板，容器是运行实例”的核心模型。

### 理解

```text
Dockerfile --docker build--> 镜像 --docker run--> 容器
远程仓库  --docker pull----> 本地镜像
```

- **镜像（Image）**：只读模板，包含程序、依赖和默认启动命令。
- **容器（Container）**：镜像的一次运行实例，有自己的进程和可写层。
- **仓库（Registry）**：保存和分发镜像，例如 Docker Hub。
- **容器主进程**：主进程结束，容器通常也会退出；容器不是一台必须长期运行的虚拟机。

### 任务

```powershell
docker pull python:3.10-slim
docker image ls
docker run --name python-check python:3.10-slim python --version
docker ps
docker ps -a
docker logs python-check
docker inspect python-check
docker rm python-check
```

### 产出与验收

- [ ] 能解释为什么 `python-check` 不出现在 `docker ps`，却出现在 `docker ps -a`
- [ ] 能从 `docker logs` 查看程序输出
- [ ] 能区分 `docker image ls` 与 `docker ps -a`

休息 10 分钟。

## 四、模块 2：容器化 Python 程序（10:40—12:00）

本目录已经提供：

- `app.py`：运行约 10 秒后退出的 Python 程序
- `Dockerfile`：描述如何构建程序镜像

### 目标

理解 Dockerfile 的基本指令，并走通“编写 → 构建 → 运行 → 验证”的流程。

### 先读懂 Dockerfile

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . /app
CMD ["python", "app.py"]
```

逐行回答：

1. 基础镜像是什么？---python:3.10-slim
2. 容器内工作目录是什么？---/app
3. 哪些本地文件被复制进了镜像？---./
4. 容器启动后默认执行什么命令？---python app.py

### 构建并运行

```powershell
docker build -t my-python-app:v1 .
docker image ls my-python-app
docker run --name python-app-v1 my-python-app:v1
docker ps -a
docker logs python-app-v1
docker inspect python-app-v1
docker rm python-app-v1
```

重新执行一次构建，观察哪些步骤显示为缓存命中。随后修改 `app.py` 中的一行输出文字，再构建 `v2`：

```powershell
docker build -t my-python-app:v2 .
docker image ls my-python-app
docker run --rm my-python-app:v2
```

### 产出与验收

- [ ] 成功构建 `my-python-app:v1` 和 `my-python-app:v2`
- [ ] 能解释 `FROM`、`WORKDIR`、`COPY`、`CMD` 的作用
- [ ] 能说明镜像标签 `v1`、`v2` 的用途
- [ ] 能解释程序执行完后容器为何变为 `Exited`

午休 60 分钟。

## 五、模块 3：端口、挂载与容器内操作（13:00—14:15）

### 目标

理解容器与宿主机如何交换网络流量和文件。

### 任务 A：进入容器观察隔离环境

```powershell
docker run --rm -it python:3.10-slim sh
```

进入后执行 `pwd`、`ls`、`python --version` 和 `cat /etc/os-release`，最后执行 `exit`。

### 任务 B：绑定挂载

```powershell
docker run --rm -v "${PWD}:/app" -w /app python:3.10-slim python app.py
```

修改本地 `app.py` 后再次运行，观察为什么不需要重新构建镜像。

### 任务 C：端口映射

```powershell
docker run --rm --name python-web -p 8000:8000 -v "${PWD}:/app" -w /app python:3.10-slim python -m http.server 8000
```

保持命令运行，在浏览器打开 `http://localhost:8000`。验证后按 `Ctrl+C` 停止容器。

### 产出与验收

- [ ] 能解释 `-it`、`--rm`、`-v`、`-w` 和 `-p` 的作用
- [ ] 能解释 `8000:8000` 左侧是宿主机端口，右侧是容器端口
- [ ] 能说出绑定挂载与 `COPY` 的区别

## 六、模块 4：容器网络（14:15—15:00）

### 目标

理解同一 Docker 网络中的容器可以使用容器名互相访问。

### 任务

```powershell
docker network create docker-lab-net
docker run -d --name web --network docker-lab-net nginx:alpine
docker run --rm --network docker-lab-net python:3.10-slim python -c "import urllib.request; print(urllib.request.urlopen('http://web').status)"
docker network inspect docker-lab-net
docker logs web
docker rm -f web
docker network rm docker-lab-net
```

### 产出与验收

- [ ] 请求返回 HTTP 状态码 `200`
- [ ] 能解释为什么访问地址是 `http://web` 而不是某个固定 IP
- [ ] 能说明 `-p` 解决宿主机访问容器，Docker 网络解决容器间通信

休息 10 分钟。

## 七、模块 5：使用 Docker Compose（15:10—16:20）

### 目标

把较长的启动命令写成可版本控制的服务配置。

### 任务

在本目录创建 `compose.yaml`，先手写下面的内容，不要只复制后直接运行：

```yaml
services:
  web:
    image: python:3.10-slim
    working_dir: /app
    command: python -m http.server 8000
    ports:
      - "8000:8000"
    volumes:
      - .:/app
```

执行：

```powershell
docker compose config
docker compose up -d
docker compose ps
docker compose logs
docker compose down
```

再次执行 `docker compose up -d`，在浏览器访问 `http://localhost:8000`，然后用 `docker compose down` 完整收尾。

### 产出与验收

- [ ] 创建并通过 `docker compose config` 校验 `compose.yaml`
- [ ] 能解释 service、image、command、ports、volumes
- [ ] 能使用 `up`、`ps`、`logs`、`down` 管理服务
- [ ] 能说出 Compose 相比多个 `docker run` 命令的优势

## 八、模块 6：故障排查练习（16:20—17:10）

### 目标

形成固定排查顺序：先看状态，再看日志，最后检查配置。

### 故意制造并修复三个问题

1. **容器名称冲突**：连续两次使用同一个 `--name`。
2. **端口冲突**：Compose 服务运行时，再启动另一个占用宿主机 `8000` 端口的容器。
3. **启动命令错误**：把 Compose 中的 `http.server` 临时写错。

每次都按下面的顺序排查：

```powershell
docker ps -a
docker compose ps
docker logs <容器名>
docker compose logs
docker inspect <容器名>
```

在学习记录中为每个错误写下：

```text
现象：
错误信息：
原因：
当前状态：
修复方式：
如何预防：
```

### 产出与验收

- [ ] 独立修复三个预设问题
- [ ] 没有用“全部删除重来”代替定位原因
- [ ] 能根据 `Exited` 状态和日志判断是程序结束还是程序出错

## 九、最终挑战与学习闭环（17:10—18:00）

### 最终挑战

不查看前面的完整命令，独立完成：

1. 构建 Python 应用镜像并添加明确标签。
2. 运行容器并查看日志。
3. 使用绑定挂载运行本地代码。
4. 通过 Compose 启动网页服务并访问它。
5. 停止服务，清理本次练习创建的容器和网络。
6. 用 100—200 字总结镜像、容器、挂载、端口和 Compose 的关系。

### Git 提交闭环

先只查看和检查当天相关改动：

```powershell
git status --short
git diff -- 01_Engineering_Tools/Docker_Practice
```

确认没有密钥、账号信息和无关文件后，只暂存 Docker 学习成果：

```powershell
git add 01_Engineering_Tools/Docker_Practice
git diff --staged
git commit -m "docs: complete one-day Docker practice"
```

推送前先用 `git branch --show-current` 确认当前分支，再执行对应的 `git push`。不要为了完成清单而提交尚未理解或未验证的内容。

### 当日完成标准

- [ ] 所有核心命令均由自己实际执行过
- [ ] `compose.yaml` 可以正常启动和关闭服务
- [ ] 三个故障都有原因与修复记录
- [ ] 最终挑战可以基本脱离文档完成
- [ ] Git 暂存内容只包含本次 Docker 学习成果

## 十、最小命令速查

| 目的 | 命令 |
|---|---|
| 查看镜像 | `docker image ls` |
| 查看运行中容器 | `docker ps` |
| 查看所有容器 | `docker ps -a` |
| 构建镜像 | `docker build -t 名称:标签 .` |
| 运行容器 | `docker run 镜像` |
| 后台运行 | `docker run -d 镜像` |
| 查看日志 | `docker logs 容器名` |
| 进入容器 | `docker exec -it 容器名 sh` |
| 停止容器 | `docker stop 容器名` |
| 删除容器 | `docker rm 容器名` |
| 删除镜像 | `docker rmi 镜像名:标签` |
| 查看详细信息 | `docker inspect 对象名` |
| 启动 Compose | `docker compose up -d` |
| 关闭 Compose | `docker compose down` |

## 十一、一天之后怎么继续

第二天再学习以下内容，避免塞进今天：

1. `.dockerignore` 与构建上下文
2. Dockerfile 分层缓存和多阶段构建
3. 命名卷与数据持久化
4. 环境变量、健康检查和重启策略
5. 非 root 用户、镜像漏洞与敏感信息管理
6. 将一个真实的 Flask 或 FastAPI 项目容器化
