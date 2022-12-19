# coding:utf-8
# Date: 2021/9/25
# Time: 12:18
# Author: Toutoutoutouer
# E-mail: wes0018@aliyun.com
# D:\Anacodar\python.exe

import re

str = '1564165165489416516351564189418941891981897489156312564189498125616515165189498156'
pattern = re.compile('\d[0-9]{2}')
while len(str) > 3:
    print(pattern.match(str).group())
    str = str.replace(pattern.match(str).group(), '')
