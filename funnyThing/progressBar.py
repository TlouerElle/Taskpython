"""

     进度条

"""

from tqdm import tqdm

result = 0
for i in tqdm(range(100000000)):
    result = result + i
    pass
print(result)
