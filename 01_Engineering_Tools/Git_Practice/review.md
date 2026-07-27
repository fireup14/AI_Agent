# Git 与 GitHub 学习总结

本文总结 Git 学习模块 1–5，作为后续开发时的复习手册和命令速查表。

## 1. Git 的核心模型

Git 保存的是一系列可追溯的项目版本。一次修改通常会经过四个位置：

```text
工作区（正在编辑的文件）
    ↓ git add
暂存区（选择下一次要提交的内容）
    ↓ git commit
本地仓库（本机保存的提交历史）
    ↓ git push
远程仓库（GitHub 上的备份和协作仓库）
```

常见文件状态：

| 状态 | 含义 |
| --- | --- |
| Untracked | 新文件，Git 尚未跟踪 |
| Modified | 已跟踪文件发生修改，但尚未暂存 |
| Staged | 修改已加入暂存区，准备提交 |
| Committed | 修改已保存为本地提交 |
| Pushed | 本地提交已推送到远程仓库 |

最重要的检查命令：

```bash
git status
```

进行切换分支、合并、提交、拉取或推送前，都可以先执行一次 `git status`。

## 2. 仓库与基础提交

### 创建或识别仓库

在普通目录中创建 Git 仓库：

```bash
git init
```

查看当前仓库根目录：

```bash
git rev-parse --show-toplevel
```

Git 命令即使在仓库子目录执行，通常仍然作用于整个仓库。本项目的仓库根目录是：

```text
E:\HelloWorld\AI_Agent
```

### 暂存修改

暂存指定文件：

```bash
git add <文件路径>
```

暂存当前目录及其子目录的所有改动：

```bash
git add .
```

学习阶段优先使用 `git add <文件路径>`，可以避免把无关文件、临时文件或敏感文件一起提交。

### 创建提交

```bash
git commit -m "docs: add git learning notes"
```

一次好的提交应当：

- 只包含同一个目的的修改；
- 提交前已经检查差异；
- 提交说明能准确描述“做了什么”；
- 不包含密码、Token、API Key 或生成文件。

### 查看历史

```bash
git log
git log --oneline
git log --oneline --decorate --graph --all
```

查看最近一次提交的作者：

```bash
git log -1 --format="作者：%an <%ae>%n说明：%s"
```

## 3. 查看差异与撤销修改

### 查看未暂存差异

```bash
git diff
git diff -- <文件路径>
```

`git diff` 默认只显示已跟踪文件的未暂存修改，不显示未跟踪文件的内容。

### 查看已暂存差异

```bash
git diff --staged
git diff --staged -- <文件路径>
```

`git diff --staged` 展示下一次 commit 将要保存的内容，是提交前最重要的检查之一。

### 取消暂存

```bash
git restore --staged <文件路径>
```

这个命令只把文件移出暂存区，不会删除工作区中的修改。

### 放弃未暂存修改

```bash
git restore <文件路径>
```

这个命令会用最近一次提交中的内容覆盖工作区修改。未提交的修改可能无法恢复，执行前必须确认文件路径和差异。

### `.gitignore`

`.gitignore` 用于排除不应提交的文件，例如：

```gitignore
# Python
__pycache__/
*.py[cod]
.venv/
venv/

# Secrets
.env
.env.*
*.pem
*.key

# Editors and system files
.vscode/
.idea/
.DS_Store
Thumbs.db

# Logs
*.log
```

`.gitignore` 通常只对尚未跟踪的文件生效。如果文件已经进入提交历史，仅把它加入 `.gitignore` 不会自动停止跟踪。

## 4. 分支

分支是一条独立的提交线。功能开发可以在新分支中完成，再合并回主分支，从而减少对稳定代码的影响。

### 查看分支

```bash
git branch
git branch -vv
git branch --show-current
git branch -a
```

`git branch -vv` 还会显示本地分支跟踪的远程分支。

### 创建和切换分支

创建并切换：

```bash
git switch -c feature/login
```

切换已有分支：

```bash
git switch master
```

只创建但不切换：

```bash
git branch feature/login
```

常见命名：

```text
feature/login       新功能
fix/login-error     缺陷修复
docs/git-review     文档修改
practice/merge      学习练习
```

### 删除分支

删除已经合并的分支：

```bash
git branch -d feature/login
```

强制删除：

```bash
git branch -D feature/login
```

`-D` 可能删除尚未合并的提交，不应随意使用。

## 5. 合并分支

合并命令的含义是：把指定分支合并到当前分支。

例如把 `feature/login` 合并进 `master`：

```bash
git switch master
git merge feature/login
```

关键是先切换到接收修改的分支。

### Fast-forward

如果主分支在功能分支创建后没有出现新提交，Git 可能执行快进合并：

```text
master: A---B
              \
feature:       C---D

合并后 master 直接移动到 D。
```

这种情况下不需要额外的合并提交。

### 合并冲突

当两个分支修改了同一文件的同一部分，Git 无法自动判断应保留哪份内容，就会暂停合并。

典型提示：

```text
CONFLICT (add/add): Merge conflict in switch.txt
Automatic merge failed; fix conflicts and then commit the result.
```

`add/add` 表示两个分支分别新增了路径相同、内容不同的文件。

冲突文件中会出现：

```text
<<<<<<< HEAD
当前分支的内容
=======
被合并分支的内容
>>>>>>> feature/nice
```

处理流程：

1. 打开冲突文件；
2. 手动整理成最终内容；
3. 删除 `<<<<<<<`、`=======`、`>>>>>>>` 标记；
4. 暂存已解决的文件；
5. 完成合并提交。

```bash
git status
git add <冲突文件>
git commit -m "resolve merge conflict"
```

如果想放弃整次合并：

```bash
git merge --abort
```

按 `Ctrl+C` 只会中断当前终端程序，不等于取消 Git 的合并状态。

在冲突解决或合并取消之前，切换分支可能出现：

```text
needs merge
error: you need to resolve your current index first
```

此时应选择完成冲突处理，或者执行 `git merge --abort`，不能直接切换分支。

## 6. 远程仓库与 GitHub

### 添加和查看远程地址

```bash
git remote add origin <GitHub 仓库 HTTPS 地址>
git remote -v
```

`origin` 只是远程地址的常用别名，不是登录账号，也不是固定关键字。

修改已有远程地址：

```bash
git remote set-url origin <新的仓库地址>
```

### 首次推送

先确认当前分支名：

```bash
git branch --show-current
```

首次推送并建立跟踪关系：

```bash
git push -u origin <主分支名>
```

例如本项目的主分支是 `master`：

```bash
git push -u origin master
```

建立跟踪关系后通常只需：

```bash
git push
git pull
```

### 获取远程更新

只获取远程信息，不修改当前工作分支：

```bash
git fetch origin
```

拉取并整合当前分支的远程更新：

```bash
git pull
```

在工作区干净、只允许快进时，可以使用：

```bash
git pull --ff-only
```

`git pull` 可以理解为先获取远程更新，再将更新整合到当前分支。多人协作时，开始工作和推送前应关注远程是否已经变化。

## 7. Git 作者身份与 GitHub 登录认证

下面三个概念互相独立：

| 内容 | 决定什么 | 查看命令 |
| --- | --- | --- |
| `origin` | 代码从哪里拉取、向哪里推送 | `git remote -v` |
| `user.name`、`user.email` | 新 commit 中记录的作者 | `git config user.name`、`git config user.email` |
| Credential Manager | 当前认证账号是否有权限访问 GitHub 仓库 | `git config --show-origin --get-all credential.helper` |

Git 本身没有统一的“登录账号”。作者信息不负责登录，远程地址也不代表认证账号。

### 设置 GitHub 作者信息

在 GitHub 的 `Settings → Emails` 页面复制经过验证的邮箱，或者 GitHub 提供的 `noreply` 邮箱，然后设置：

```bash
git config --global user.name "<GitHub 用户名或展示名称>"
git config --global user.email "<GitHub 邮箱或 noreply 邮箱>"
```

GitHub noreply 邮箱通常类似：

```text
数字ID+用户名@users.noreply.github.com
```

应从 GitHub 设置页面复制，不要猜测数字 ID。

### 配置层级

常见配置层级及覆盖关系：

```text
system（系统）
    ↓ 被覆盖
global（当前操作系统用户）
    ↓ 被覆盖
local（当前仓库）
```

查看配置来源：

```bash
git config --show-origin --show-scope --get-regexp "^user\.(name|email)$"
```

查看当前仓库的局部配置：

```bash
git config --local --get user.name
git config --local --get user.email
```

删除不再需要的仓库级作者覆盖：

```bash
git config --local --unset user.name
git config --local --unset user.email
```

修改作者配置只影响未来创建的提交，不会自动修改已有提交。

### HTTPS 认证

Git for Windows 通常通过 Git Credential Manager 保存 GitHub 的浏览器登录授权。它负责认证和权限，不会把 Token 写入 commit。

不要把 GitHub Token 写入：

- Git 远程 URL；
- 源代码；
- `.env` 以外的普通配置文件；
- README、日志或截图；
- commit 信息。

## 8. 每次学习后的固定同步流程

### 开始前

```bash
cd E:\HelloWorld\AI_Agent
git switch master
git status
git pull --ff-only
```

### 学习完成后

```bash
git status
git diff
git add <本次相关文件>
git diff --staged
git commit -m "docs: describe this learning result"
git push
git status
```

流程含义：

1. `git status`：确认分支和文件状态；
2. `git diff`：检查工作区修改；
3. `git add <文件>`：只选择本次相关内容；
4. `git diff --staged`：确认即将提交的准确内容；
5. `git commit`：创建本地版本；
6. `git push`：上传本地提交；
7. 再次 `git status`：确认工作区干净且分支已同步。

完成后的理想状态：

```text
On branch master
Your branch is up to date with 'origin/master'.
nothing to commit, working tree clean
```

## 9. 提交信息规范

常用前缀：

| 前缀 | 用途 | 示例 |
| --- | --- | --- |
| `feat:` | 新功能、新练习 | `feat: add calculator exercise` |
| `docs:` | 文档、笔记 | `docs: add git review` |
| `fix:` | 修复错误 | `fix: handle empty input` |
| `refactor:` | 不改变功能的代码整理 | `refactor: simplify parser` |
| `chore:` | 配置和维护 | `chore: update gitignore` |
| `test:` | 测试相关修改 | `test: add login validation cases` |

提交说明应使用明确的动词和对象，避免：

```text
修改
更新一下
test
完成
```

更清晰的示例：

```text
docs: summarize git branch workflow
fix: resolve duplicate navigation entry
chore: ignore local environment files
```

## 10. 常见问题与处理

### `nothing to commit, working tree clean`

表示当前没有尚未提交的修改，不是报错。

### `remote origin already exists`

表示已经存在名为 `origin` 的远程地址。先查看：

```bash
git remote -v
```

如需修改：

```bash
git remote set-url origin <正确地址>
```

### `src refspec main does not match any`

常见原因是本地主分支并不叫 `main`，或者仓库还没有任何提交。先检查：

```bash
git branch --show-current
git log --oneline
```

使用实际分支名推送，例如：

```bash
git push -u origin master
```

### 推送被拒绝：`non-fast-forward`

通常说明远程出现了本地没有的提交。不要直接强制推送。先执行：

```bash
git status
git fetch origin
git branch -vv
```

确认远程变化后，再选择合适的拉取和整合方式。

### LF/CRLF 警告

Windows 中可能出现：

```text
LF will be replaced by CRLF the next time Git touches it
```

这是换行符转换提示，不是合并失败的原因。真正导致合并停止的错误通常会包含 `CONFLICT`。团队项目可以通过 `.gitattributes` 统一换行规则。

### 无法切换分支：`needs merge`

说明仓库仍处于冲突状态。执行：

```bash
git status
```

然后完成冲突并提交，或者：

```bash
git merge --abort
```

## 11. 安全注意事项

- 绝不提交密码、API Key、Token、私钥或 `.env`；
- 推送前执行 `git status` 和 `git diff --staged`；
- `.gitignore` 不是密钥保险箱，已经提交的密钥仍存在于历史中；
- 不随意使用 `git branch -D`；
- 不随意使用强制推送；
- 不随意使用会丢弃修改的 `git restore <文件>`；
- 不使用 `git reset --hard` 处理不理解的问题；
- 出现冲突先查看 `git status`，不要连续尝试不理解的命令；
- 删除或覆盖前确认仓库根目录、当前分支和目标文件。

如果密钥已经提交并推送，应立即在服务端撤销或轮换密钥；仅从当前文件中删除并不能消除历史泄露风险。

## 12. 常用命令速查

```bash
# 状态与历史
git status
git log --oneline
git log --oneline --decorate --graph --all
git rev-parse --show-toplevel

# 差异与暂存
git diff
git diff --staged
git add <文件路径>
git restore --staged <文件路径>
git restore <文件路径>

# 提交
git commit -m "说明"
git log -1 --format="作者：%an <%ae>%n说明：%s"

# 分支
git branch
git branch -vv
git branch --show-current
git switch -c <新分支>
git switch <已有分支>
git branch -d <已合并分支>

# 合并
git merge <分支名>
git merge --abort

# 远程
git remote -v
git remote add origin <仓库地址>
git remote set-url origin <仓库地址>
git fetch origin
git pull --ff-only
git push
git push -u origin <主分支名>

# 作者配置
git config user.name
git config user.email
git config --global user.name "<名称>"
git config --global user.email "<邮箱>"
git config --show-origin --show-scope --get-regexp "^user\.(name|email)$"
```

## 13. 最终自检

- [ ] 能解释工作区、暂存区、本地仓库和远程仓库；
- [ ] 能识别 Untracked、Modified、Staged 和 Committed；
- [ ] 提交前会检查 `git status`、`git diff` 和 `git diff --staged`；
- [ ] 能创建、切换、合并和安全删除分支；
- [ ] 能解决基础冲突，知道 `Ctrl+C` 不等于 `git merge --abort`；
- [ ] 能区分 `origin`、Git 作者信息和 GitHub 登录认证；
- [ ] 能配置正确的 GitHub noreply 邮箱；
- [ ] 能首次推送并理解 `-u` 的作用；
- [ ] 能执行固定的“检查、提交、推送、验证”流程；
- [ ] 能识别敏感文件并避免将其提交到仓库。

