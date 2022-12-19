# coding:utf-8
# Date: 2021/9/28
# Time: 18:39
# Author: Toutoutoutouer
# E-mail: wes0018@aliyun.com
# D:\Anacodar\python.exe
import re
str = 'happiness is a way station between too much and too little.'
pattern = re.compile('a|b')
print(pattern.sub('china', str))
