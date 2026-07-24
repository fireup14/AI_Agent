# Git 版本控制实践库

本文件夹用于你练习 Git 的日常工作流。

## 🛠️ 推荐练习步骤

1. **初始化本地仓库**：
   ```bash
   git init
   ```
2. **配置个人信息**：
   ```bash
   git config user.name "你的名字"
   git config user.email "你的邮箱"
   ```
3. **日常代码提交流**：
   - 编写或修改文件后，查看状态：`git status`
   - 将文件添加到暂存区：`git add .`
   - 提交到本地仓库：`git commit -m "feat: init git practice"`
4. **分支操作（重点）**：
   - 创建新分支：`git branch feature/git-test`
   - 切换到新分支：`git checkout feature/git-test`
   - 在新分支上做一些修改并提交。
   - 切回主分支：`git checkout master` (或 `main`)
   - 将新分支的修改合并过来：`git merge feature/git-test`
5. **冲突解决（加深理解）**：
   - 在两个不同的分支上修改同一个文件的同一行代码，然后尝试合并，观察并手动解决冲突（Conflict）。
