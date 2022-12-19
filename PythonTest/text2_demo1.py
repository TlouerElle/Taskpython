import random
num1 = random.randint(1,10)
num2 = eval(input('请输入数字:'))
if num1 == num2:
    print('猜对了')
elif num1 > num2:
    print('猜小了')
elif num1 < num2:
    print('猜大了')