#!/usr/bin/env bash
set -e

# 进入仓库目录
cd "$(dirname "$0")"

# 1. 执行脚本自动同步最新日期与看板状态
python3 scripts/update_readme.py

# 2. 检查是否有变动并提交推送
git add README.md
if git diff --staged --quiet; then
  echo ">>> README.md 日期已是最新，无需重复提交。"
else
  CURRENT_DATE=$(date +'%Y-%m-%d')
  git commit -m "docs: 账号维护状态与最新日期同步 ($CURRENT_DATE)"
  git push origin main
  echo ">>> [成功] 已完成本地更新并推送至 GitHub！"
fi
