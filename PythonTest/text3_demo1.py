for i in range(3):
    username = input("请输入用户名：")
    password = eval(input("请输入密码："))
    if username == "123456" and password == 123456:
        print("----------欢迎购物----------")
        break
    else:
        print("账号或密码错误,你还剩下" + str(2-i) + "次机会")
        while i == 2:
            print("用户名或密码有误")
            break