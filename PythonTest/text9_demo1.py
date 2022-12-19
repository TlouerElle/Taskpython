import random


class Login:
    def __init__(self, username, pwd):
        self.username = username
        self.pwd = pwd
        code = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
        self.verification_code = code[random.randint(0, 62)] + code[random.randint(0, 62)] + code[
            random.randint(0, 62)] + code[random.randint(0, 62)]
        print(self.verification_code)

    def get_username(self):
        return self.username

    def check_pwd(self):
        if 8 <= len(self.pwd) < 20:
            if self.pwd.isalpha():
                return False
            if self.pwd.isdigit():
                return False
            else:
                return True
        else:
            return False

    def check_verificationcode(self):
        if self.verification_code == inputcode:
            print('验证码正确')
        else:
            print('验证码错误')


login = Login(input('请输入用户名:'), input('请输入密码:'))
inputcode = input('请输入验证码:')
print(login.get_username())
print(login.check_pwd())
login.check_verificationcode()
