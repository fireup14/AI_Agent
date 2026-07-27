# Git 与 GitHub 学习大纲

本目录用于学习 AI 项目开发中的版本控制协作流程。完成本大纲后，你应能将整个 `AI_Agent` 文件夹安全发布到 GitHub，并在每次学习结束后完成一次清晰、可追溯的提交与推送。

## 学习目标

1. 理解 Git 的工作区、暂存区、本地仓库和远程仓库。
2. 能够查看改动、选择性暂存、编写规范提交，并查看历史与回退指定改动。
3. 熟练使用分支开发、合并分支，并能处理基础冲突。
4. 创建 GitHub 仓库，将本地 `AI_Agent` 项目首次推送到远程。
5. 建立每次学习后的固定同步流程，保护密钥和不应上传的本地文件。

## 核心概念

```text
工作区（修改文件）
    ↓ git add
暂存区（选择本次提交的内容）
    ↓ git commit
本地仓库（保存历史版本）
    ↓ git push
GitHub 远程仓库（备份、协作、展示）
```

## 学习模块

### 模块 1：本地版本控制基础

学习内容：`git status`、`git add`、`git commit`、`git log`、`.gitignore`。

练习任务：

1. 在本目录修改或新建一个练习文件。
2. 用 `git status` 区分“未跟踪”“已修改”“已暂存”三种状态。
3. 分别用 `git add <文件名>` 与 `git add .` 暂存文件，理解两者区别。
4. 创建一次提交，例如：`git commit -m "docs: add git learning outline"`。
5. 使用 `git log --oneline` 查看提交历史。

完成标准：能解释一次文件修改从工作区到 GitHub 所经过的四个位置。

### 模块 2：查看差异与撤销操作

学习内容：`git diff`、`git diff --staged`、`git restore`、`git restore --staged`。

练习任务：

1. 修改文件后，用 `git diff` 查看尚未暂存的差异。
2. 暂存后，用 `git diff --staged` 查看准备提交的内容。
3. 对一个无用的未暂存修改执行 `git restore <文件名>`。
4. 对一个误暂存文件执行 `git restore --staged <文件名>`，确认文件内容不会丢失。

完成标准：提交前能先检查差异；知道 `restore` 与历史回退不同，不会随意使用破坏性命令。

### 模块 3：分支、合并与冲突

学习内容：`git switch -c`、`git switch`、`git branch`、`git merge`。

练习任务：

1. 创建练习分支：`git switch -c practice/git-branch`。
2. 在分支中修改一个文件并提交。
3. 切回主分支并合并：`git switch main`、`git merge practice/git-branch`。
4. 在两个分支修改同一文件的同一行，制造一次冲突；理解冲突标记、手动保留正确内容、重新 `add` 与 `commit` 的流程。

完成标准：能在不影响主分支的情况下完成一项小练习，并将其合并回来。

### 模块 4：发布 `AI_Agent` 到 GitHub

学习内容：GitHub 仓库、远程地址 `origin`、Git 作者身份、GitHub 登录认证、`git push`、`git pull`。

首次发布流程：

1. 在 GitHub 网站创建一个空仓库，例如 `AI_Agent`；不要勾选自动创建 README、`.gitignore` 或 License，避免与本地历史冲突。
2. 在项目根目录确认当前状态：`git status`。
3. 在根目录创建并检查 `.gitignore`，确保不会提交以下敏感或本地生成文件：`.env`、API Key、虚拟环境、`__pycache__/`、日志、模型权重与大型数据集。
4. 提交希望公开的学习代码和文档。
5. 添加远程仓库：`git remote add origin <你的 GitHub 仓库地址>`。
6. 使用 `git branch --show-current` 确认主分支名后首次推送：`git push -u origin <主分支名>`。
7. 在 GitHub 网页确认文件、提交记录与 README 显示正常。

账号与配置：

Git 的远程地址、提交作者和登录认证是三个相互独立的概念：

| 配置 | 作用 | 查看方式 |
| --- | --- | --- |
| `origin` | 指定代码拉取和推送的远程仓库地址 | `git remote -v` |
| `user.name`、`user.email` | 写入新 commit 的作者名称和邮箱 | `git config user.name`、`git config user.email` |
| Credential Manager | 保存 GitHub HTTPS 登录授权，决定当前账号是否有权推送 | `git config --show-origin --get-all credential.helper` |

`origin` 只是远程地址的常用别名，不代表登录账号。首次执行 `git push -u origin <主分支名>` 后，本地分支会跟踪对应的远程分支；以后通常可以直接执行 `git push` 和 `git pull`。

Git 本身没有统一的“登录账号”。`user.name` 和 `user.email` 只标记提交作者，并不参与 GitHub 登录。为了让命令行提交正确关联到 GitHub 账号，可以在 GitHub 的 `Settings → Emails` 页面复制经过验证的邮箱，或使用 GitHub 提供的 `noreply` 邮箱，然后设置全局作者信息：

```bash
git config --global user.name "<你的 GitHub 用户名或展示名称>"
git config --global user.email "<你的 GitHub 邮箱或 noreply 邮箱>"
```

配置分为 `system`、`global` 和 `local` 三个常见层级；仓库的 `local` 配置会覆盖用户级的 `global` 配置。使用以下命令检查实际生效的作者信息及其来源：

```bash
git config --show-origin --show-scope --get-regexp "^user\.(name|email)$"
git log -1 --format="作者：%an <%ae>"
```

如果某个仓库仍保留旧的作者配置，可以先查看：

```bash
git config --local --get user.name
git config --local --get user.email
```

确认不再需要后，删除仓库级覆盖，让它继承新的全局配置：

```bash
git config --local --unset user.name
git config --local --unset user.email
```

修改作者配置只影响未来创建的提交，不会自动修改已有提交的作者信息。

> 安全规则：绝不提交 API Key、密码、Token 或 `.env` 文件。即使仓库设为私有，也应把密钥保留在本地环境变量中。

完成标准：能够在 GitHub 网页看到完整项目、提交历史和本 README；能够解释 `origin`、提交作者与登录认证的区别，并确认新提交已关联到正确的 GitHub 作者信息。

### 模块 5：每次学习后的固定同步流程

每次完成一个学习任务后，在项目根目录执行：

```bash
git status
git diff
git add <本次完成的文件>
git commit -m "feat: complete <学习主题>"
git push
```

提交信息建议使用以下前缀：

| 前缀 | 使用场景 | 示例 |
| --- | --- | --- |
| `feat:` | 新增练习、功能或示例 | `feat: add numpy broadcasting exercise` |
| `docs:` | 更新计划、笔记或 README | `docs: record git learning notes` |
| `fix:` | 修复代码错误 | `fix: handle empty todo list` |
| `refactor:` | 不改变行为的代码整理 | `refactor: simplify calculator module` |
| `chore:` | 配置或杂项维护 | `chore: update gitignore` |

完成标准：每次推送前知道哪些文件将被上传，并能用一条提交信息说明本次学习产出。

## 建议学习顺序

| 顺序 | 内容 | 建议产出 |
| --- | --- | --- |
| 1 | 模块 1 | 1–2 个本地提交 |
| 2 | 模块 2 | 一次差异检查与撤销练习记录 |
| 3 | 模块 3 | 一个合并完成的练习分支 |
| 4 | 模块 4 | GitHub 上的 `AI_Agent` 仓库 |
| 5 | 模块 5 | 后续每次学习一次小而清晰的提交 |

## 常用命令速查

```bash
git status                 # 查看当前状态
git diff                   # 查看未暂存改动
git add <文件名>            # 暂存指定文件
git commit -m "说明"        # 创建本地提交
git log --oneline          # 简洁查看提交历史
git switch -c <分支名>      # 创建并切换分支
git switch <分支名>         # 切换分支
git merge <分支名>          # 合并分支
git remote -v              # 查看远程仓库地址
git pull                   # 拉取远程更新
git push                   # 推送本地提交到 GitHub
```

## 学习完成检查清单

- [ ] 我能解释工作区、暂存区、本地仓库与远程仓库。
- [ ] 我能检查差异并只暂存本次学习相关的文件。
- [ ] 我能创建、切换、合并分支并处理一次简单冲突。
- [ ] 我已为整个 `AI_Agent` 项目配置好 `.gitignore`。
- [ ] 我已将项目首次推送到 GitHub。
- [ ] 我建立了“学习完成 → 检查 → 提交 → 推送”的习惯。
