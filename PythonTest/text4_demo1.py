print("***斐波那契数列***")
n = eval(input("请输入项数n="))
num1 = 1
num2 = 0
while n > 0 :
    result = num1 + num2
    num1 = num2
    num2 = result
    n -= 1
    print(result, end=" ")