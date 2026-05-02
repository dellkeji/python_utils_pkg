# Python Utils PKG — AI 工作流

## 触发命令

写完代码后，对 小仔 说：

> **"review and commit"**

小仔会按以下流程执行。

---

## 流程

### Step 1 — 识别改动
- `git diff` 或 `git status` 获取所有变更文件
- 读取每个改动的 Python 文件

### Step 2 — AI Code Review
Review 检查清单：

| 维度 | 检查点 |
|------|--------|
| **正确性** | 逻辑是否正确？边界情况是否处理？ |
| **健壮性** | 异常处理是否充分？输入校验是否完善？ |
| **风格** | 是否符合 PEP8？类型注解是否完整？ |
| **性能** | 是否有明显的性能问题？ |
| **安全性** | 是否有注入、密钥泄露等风险？ |
| **测试** | 是否有关联的测试文件需要更新？ |

### Step 3 — 结果判定

**✅ 通过** → 直接进入 Step 4

**⚠️ 有小问题** → 指出问题 → 你修改后再说一遍 "review and commit"

**❌ 大问题** → 详细说明问题，建议重构方向

### Step 4 — 提交
```bash
git add <changed files>
git commit -m "<AI 生成的规范 commit message>"
git push origin main
```

---

## Commit 规范

遵循 [Conventional Commits](https://www.conventionalcommits.org/)：

```
feat: 新功能
fix: 修复 bug
refactor: 重构
test: 测试相关
docs: 文档
style: 格式调整
chore: 杂项
```

---

## 项目信息

| 项目 | 值 |
|------|-----|
| 仓库 | `github.com/dellkeji/python_utils_pkg` |
| 认证 | `gh` CLI 已登录 |
| 语言 | Python 3 |
| 测试 | `pytest` |
| 格式化 | `black` |
