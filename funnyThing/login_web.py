# coding:utf-8
# Date: 2021/9/6
# Time: 16:14
# Author: Toutoutoutouer
# E-mail: wes0018@aliyun.com
# D:\Anacodar\python.exe

import requests

# 登录地址
url = 'http://10.1.2.3'

# 构造头部信息
header = {
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Cookie': 'PHPSESSID=mctia32agd0l5tujkfcq4fhm90',
    'Host': '10.1.2.3',
    'Referer': 'http://10.1.2.3/a79.htm?isReback=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38',
    'X-Requested-With': 'XMLHttpRequest',
}

# 构造登录数据
data = {
    'callback': 'dr1631019759546',
    'DDDDD': '2019110300122',
    'upass': '250018',
    '0MKKey': '123456',
    'R1': '0',
    'R3': '1',
    'R6': '0',
    'para': '00',
    'v6ip': '_: 1631019747885',
}
# 发送post请求登录网页
response = requests.post(url, data=data, headers=header)
print(response)