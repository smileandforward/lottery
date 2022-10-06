#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Create by H
# Create on 2022/9/15

from bs4 import BeautifulSoup

html = """
<html><head><title>haha,The Dormouse's story</tittle></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
# print(soup)    # 输出解析的html对象p
# print(soup.prettify())      # 格式化
print(soup.title)             # 输出标题<title>，eg: <title>haha,The Dormouse's story</title>
print(soup.title.string)      # 输出title标题的内容字符串
print(soup.title.parent.name) # 输出<title>节点父节点的名字

print(soup.find_all('a')) # 输出所有标签<a>组成的list
print(soup.find(id='link3')) # 返回包含id='link3'的标签所有内容