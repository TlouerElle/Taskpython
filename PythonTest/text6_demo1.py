def login(i):
    username = input("请输入用户名：")
    password = input("输入密码：")
    if username == 'admin' and password == '123456':
        print("login success!!!")
        exit()
    else:
        print("login failed!!!")
        while i == 2:
            print("系统锁定,已退出")
            exit()
for i in range(3):
    login(i)