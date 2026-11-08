#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日自动更新 README 状态和维护时间的脚本
支持 UTC+8 北京时间转换
"""
import os
import re
from datetime import datetime, timezone, timedelta

def get_beijing_time():
    beijing_tz = timezone(timedelta(hours=8))
    return datetime.now(beijing_tz)

def update_readme():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    readme_path = os.path.join(repo_root, "README.md")
    
    if not os.path.exists(readme_path):
        print(f"Error: {readme_path} not found.")
        return False
        
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    now = get_beijing_time()
    date_iso = now.strftime("%Y-%m-%d")
    date_cn = now.strftime("%Y年%m月%d日")
    badge_date = now.strftime("%Y--%m--%d")
    
    # 替换日期标签
    content = re.sub(
        r'<!-- AUTO_UPDATE_DATE_START -->.*?<!-- AUTO_UPDATE_DATE_END -->',
        f'<!-- AUTO_UPDATE_DATE_START -->{date_iso}<!-- AUTO_UPDATE_DATE_END -->',
        content,
        flags=re.DOTALL
    )
    
    content = re.sub(
        r'<!-- AUTO_UPDATE_CN_START -->.*?<!-- AUTO_UPDATE_CN_END -->',
        f'<!-- AUTO_UPDATE_CN_START -->{date_cn}<!-- AUTO_UPDATE_CN_END -->',
        content,
        flags=re.DOTALL
    )
    
    # 替换徽章中的日期
    content = re.sub(
        r'<!-- AUTO_UPDATE_BADGE_START -->.*?<!-- AUTO_UPDATE_BADGE_END -->',
        f'<!-- AUTO_UPDATE_BADGE_START -->![Last Update](https://img.shields.io/badge/每日自动维护-{badge_date}-brightgreen?style=flat-square&logo=github-actions&logoColor=white)<!-- AUTO_UPDATE_BADGE_END -->',
        content,
        flags=re.DOTALL
    )

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Successfully updated README.md with date: {date_iso} ({date_cn})")
    return True

if __name__ == "__main__":
    update_readme()
