# coding:utf-8
# Date: 2021/9/28
# Time: 18:24
# Author: Toutoutoutouer
# E-mail: wes0018@aliyun.com
# D:\Anacodar\python.exe
import re
import requests
url = 'http://blog.sina.com.cn/s/blog_147f99d5d0102vmyi.html'
response = requests.get(url)
response.encoding = 'utf-8'
if response.status_code == 200:
    pattern = re.compile('[0-9|a-z|A-Z]*@163.com|[0-9|a-z|A-Z]*@qq.com|[0-9|a-z|A-Z]*@126.com')
    list = pattern.findall(response.text)
    print(list)