import os
import re
try:
    os.rename('E:mypro/Python/text12.txt','E:mypro/Python/text122.txt')
except Exception:
    print('错误')
else:
    print('修改成功')