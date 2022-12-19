import os
import random

nums = '1234567890'
letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
stream = open(r'E:\mypro\Python\text12.txt', 'a', encoding='utf-8')
try:
    if stream.writable():
        i = 1
        while i < 100000:
            i += 1
            result = random.sample(nums, 2)[0] + random.sample(nums, 2)[1] + random.sample(letters, 2)[0] + random.sample(letters, 2)[1] + '_'
            stream.writelines(result+'\n')
    print('写入完成')

except Exception:
    print('写入失败,退出')
    exit()

stream.close()
