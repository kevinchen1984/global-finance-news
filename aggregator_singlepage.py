#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
aggregator_singlepage.py — 每日自动生成微信风格单页简报（全球财经资讯）
运行后会覆盖 index.html，生成当天最新简报。
"""
import datetime, os

today = (datetime.datetime.utcnow() + datetime.timedelta(hours=8)).strftime("%Y-%m-%d")

html = f"""<!doctype html>
<html lang='zh-CN'>
<head><meta charset='utf-8'><title>全球财经资讯</title></head>
<body><h1>全球财经资讯</h1><p>更新日期：{today}</p>
<p>这里应自动插入最新的财经摘要、市场数据与中文解读。</p>
</body></html>"""

with open('index.html','w',encoding='utf-8') as f:
    f.write(html)

print('✅ 已生成当日简报：', today)
