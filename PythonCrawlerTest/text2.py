# coding:utf-8
# Date: 2021/9/17
# Time: 17:26
# Author: Toutoutoutouer
# E-mail: wes0018@aliyun.com
# D:\Anacodar\python.exe
import requests
from bs4 import BeautifulSoup


def download_html():
    url = 'https://www.shanghairanking.cn/rankings/arwu/2021'
    response = requests.get(url)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        stream = open(r'E:\mypro\crawler\download_html.txt', 'a', encoding='utf-8')
        if stream.writable():
            stream.writelines(str(soup))
            print('^_^成功下载到E:/mypro/crawler/download_html.txt')


def analysis():
    stream = open(r'E:\mypro\crawler\download_html.txt', 'r', encoding='utf-8')
    if stream.readable():
        html = stream.read()
        soup = BeautifulSoup(html, 'html.parser')
        try:
            for tr in soup.tbody:
                stream = open(r'E:\mypro\crawler\result.txt', 'a', encoding='utf-8')
                if stream.writable():
                    stream.writelines(str(tr.div.string).strip() + ' ')
                    stream.writelines(str(list(tr.children)[1].div.div.img.attrs['alt']).strip() + ' ')
                    stream.writelines(str(list(tr.children)[2].text).strip() + ' ')
                    stream.writelines(str(list(tr.children)[3].text).strip() + ' ')
                    stream.writelines(str(list(tr.children)[4].text).strip() + '\n')
            print('^_^成功写入E:/mypro/crawler/result.txt')
        except:
            print('-_-写入失败')


download_html()
analysis()
