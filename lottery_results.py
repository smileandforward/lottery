#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Create by H
# Create on 2022/9/14

import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        return response.text
    else:
        print('无数据！')
    return None

def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    tr = soup.select('tr')[2]
    print(tr.contents)
    # tr = soup.find_all("tr")
    # print(soup.find_all("tr"))
    # print(tr[2])

if __name__=='__main__':
    # url = 'http://kaijiang.zhcw.com/zhcw/html/3d/list_2.html'
    # html = get_html(url)
    # con = parse_html(html)
    # for item in con:
    #     print(item['time'])
    #     print( item['issue'])
    #     print( item['digits'])
    #     print( item['ten_digits'])
    #     print( item['hundred_digits'])
    #     print( item['single_selection'])
    #     print( item['three_selection'])
    #     print( item['six_selection'])
    #     print( item['sales'])
    #     print( item['return_rates'])
    url = 'https://www.zhcw.com/kjxx/ssq/'
    html = get_html(url)
    con = parse_html(html)
    print(con)














































