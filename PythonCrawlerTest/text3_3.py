# coding:utf-8
# Date: 2021/9/28
# Time: 17:17
# Author: Toutoutoutouer
# E-mail: wes0018@aliyun.com
# D:\Anacodar\python.exe
import re
import requests
str = 'snauiodnjnjk电话：15346798956mklmsalkmdpoasmdpoasmddjsaiopdjnmaiosjd'
pattern = re.compile('[1-9]{11}')
list = [pattern.search(str).group()]
print(list)