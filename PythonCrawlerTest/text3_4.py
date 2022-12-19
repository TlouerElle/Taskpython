# coding:utf-8
# Date: 2021/9/28
# Time: 17:35
# Author: Toutoutoutouer
# E-mail: wes0018@aliyun.com
# D:\Anacodar\python.exe
import re
import requests
url = 'http://idcard.miaochaxun.com/'
response = requests.get(url)
if response.status_code == 200:
    pattern = re.compile('[0-9|X]{18}')
    list = pattern.findall(response.text)
    print(list)