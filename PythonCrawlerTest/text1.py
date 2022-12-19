# coding:utf-8
# Date: 2021/9/6
# Time: 15:38
# Author: Toutoutoutouer
# E-mail: wes0018@aliyun.com
# D:\Anacodar\python.exe

import requests
from bs4 import BeautifulSoup

url = 'http://search.zongheng.com'
response = requests.get(url)
response.encoding = 'utf-8'
if response.status_code == 200:
    bs = BeautifulSoup(response.content, 'html.parser')
    print(bs.prettify())
    stream = open(r'E:\mypro\crawler\file_main.txt', 'a', encoding='utf-8')
    if stream.writable():
        stream.writelines(bs.title.text)
        for i in bs.find_all('a'):
            stream.writelines(str(i.string) + i['href'] + '\n')
        print('写入完成')
    search = '/?keyword=门马'
    response = requests.get(url + search)
    if response.status_code == 200:
        bs = BeautifulSoup(response.content, 'html.parser')
        stream = open(r'E:\mypro\crawler\file_search.txt', 'a', encoding='utf-8')
        if stream.writable():
            for j in bs.find_all('a'):
                stream.writelines(str(j.string) + j['href']+ '\n')
            for i in bs.find_all('div'):
                stream.writelines(i.text)
            print('写入成功')
