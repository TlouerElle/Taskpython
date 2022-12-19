import pymysql


def login():
    print('=' * 20 + '登录' + '=' * 20)
    username = input('请输入账户名:')
    conn = pymysql.connect(host='localhost', user='root', password='223366', database='bookDB122', port=3306)
    cursor = conn.cursor()
    sql = "SELECT * FROM login WHERE username='{}' ".format(username)
    cursor.execute(sql)
    loginpassword = cursor.fetchall()
    password = input('请输入密码:')
    if loginpassword:
        if password == loginpassword[0][1]:
            print(loginpassword[0][1])
            print('登录成功!')
            conn.close()
        else:
            print('登陆失败!程序退出!')
            conn.close()
            exit()
    else:
        print('该账户不存在!!!')
        exit()
        conn.close()


class Student:

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        msg = "学生信息：id=" + self.id + ",name=" + self.name + ",age=" + self.age
        return msg

    # 获取id
    def getId(self):
        return self.id

    # 获取name
    def getName(self):
        return self.name

    # 获取age
    def getAge(self):
        return self.age

    # 设置name
    def setName(self, name):
        self.name = name

    # 设置age
    def setAge(self, age):
        self.age = age


# 添加学生信息
def addStu():
    "添加学生信息"
    id = input("请输入学生学号：")
    conn = pymysql.connect(host='localhost', user='root', password='223366', database='bookDB122', port=3306)
    cursor = conn.cursor()
    sql = "SELECT * FROM stu WHERE id='%s' "
    cursor.execute(sql)
    stu = cursor.fetchone()
    if stu :
        if id == stu[0][0]:
            print("该学号已存在，不能重复添加")
        conn.close()
        return
    name = input("请输入学生姓名：")
    age = input("请输入学生年龄：")
    sql = "insert stu(id,name,age) values('{}','{}','{}')".format(id, name, age)
    cursor.execute(sql)  # 把单个学生添加到总列表中
    # 向数据库提交
    conn.commit()
    # 关闭连接
    conn.close()
    print("添加成功:")


# 删除学生信息
def delStu():
    "删除学生信息"
    id = input("请输入要删除的学生学号：")
    conn = pymysql.connect(host='localhost', user='root', password='223366', database='bookDB122', port=3306)
    cursor = conn.cursor()
    sql = "delete from stu where id={}".format(id)
    try:
        cursor.execute(sql)
        # 向数据库提交
        conn.commit()
        conn.close()
        return 0
    except Exception as e:
        conn.rollback()
        conn.close()
        print(e)
        return 1


# 修改学生信息
def updateStu():
    id = input("请输入要修改的学生学号：")
    conn = pymysql.connect(host='localhost', user='root', password='223366', database='bookDB122', port=3306)
    cursor = conn.cursor()
    sql = "select * from stu where id={}".format(id)
    cursor.execute(sql)
    stu = cursor.fetchone()
    if stu is not None:
        if id == stu[0]:
            name = input("请输入要修改的学生姓名：")
            age = input("请输入要修改的学生年龄：")
            sql = "update stu set name='{}',age='{}' where id='{}'".format(name, age, id)
            try:
                cursor.execute(sql)
                conn.commit()
                conn.close()
                print("修改成功")
            except Exception as e1:
                # 发生错误时回滚
                conn.rollback()
                conn.close()
                print("修改失败")
                print(e1)
            return
    print("找不到该学号，没法修改")


# 查询学生信息
def selectStu():
    "查询学生信息"
    id = input("请输入要查询的学生学号：")
    conn = pymysql.connect(host='localhost', user='root', password='223366', database='bookDB122', port=3306)
    cursor = conn.cursor()
    sql = "select * from stu where id={}".format(id)
    cursor.execute(sql)
    stu = cursor.fetchone()
    if stu is not None:
        print(stu)
    else:
        print("查询失败，查不到该学生信息")


login()
print("==" * 18)
print("         欢迎使用学生管理系统         ")
print("         1.添加学生信息         ")
print("         2.删除学生信息         ")
print("         3.修改学生信息         ")
print("         4.查询学生信息         ")
print("         5.退出系统")
print("==" * 18)
flag = 0

while flag != 1:
    step = input("请输入你的操作：")
    step = int(step)
    if step == 1:
        addStu()
    elif step == 2:
        num = delStu()
        if num == 0:
            print("删除成功")
        elif num == 1:
            print("删除失败")
    elif step == 3:
        updateStu()
    elif step == 4:
        conn = pymysql.connect(host='localhost', user='root', password='223366', database='bookDB122', port=3306)
        cursor = conn.cursor()
        cursor.execute('select * from stu')
        for index in cursor.fetchall():
            print(index)
        selectStu()
    elif step == 5:
        flag = 1
    else:
        print("输入指令错误，请重新输入！！")
print("退出系统成功")
