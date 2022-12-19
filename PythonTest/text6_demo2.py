def Evensum(n):
    result = 0
    for i in range(2, n+1, 2):
        result = i + result
    print(result)
Evensum(eval(input('请输入n=')))