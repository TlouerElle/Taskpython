# coding:utf-8
# Date: 2021/9/26
# Time: 23:01
# Author: Toutoutoutouer
# E-mail: wes0018@aliyun.com
# D:\Anacodar\python.exe

import re
str = '<a>第一个a中内容</a><a>第二个</a><a>第3个text</a><a>123sdfasadas3212</a><a>dasdasdasaa313212</a><a>dasdasdasd2</a><a>dasdsadasdas13212</a>sad561as561d6a5s1d563asa1d56a1d56'
pattern = re.compile(r'[^<\a>]*[^<\/a>]')
print(pattern.findall(str))

