class Person:
    def __init__(self, name, num, money):
        self.name = name
        self.num = num
        self.money = money

    def __str__(self):
        return '{}的工号为{}本月工资为{}'.format(self.name, self.num, self.money)


class Worker(Person):
    def __init__(self, work_time, time, name, num, money):
        super().__init__(name, num, money)
        self.work_time = work_time
        self.time = time
        self.money = self.work_time * self.time


class Salesman(Person):
    def __init__(self, sales_volume, proportion, name, num, money):
        super().__init__(name, num, money)
        self.sales_volume = sales_volume
        self.proportion = proportion
        self.money = self.proportion * self.sales_volume


class Manager(Person):
    def __init__(self, name, num, money):
        super().__init__(name, num, money)
        self.money = money


class Salesmanager(Salesman,Manager,Person):
    def __init__(self, name, num, money, sales_volume, proportion):
        super().__init__(sales_volume, proportion, name, num, money)
        self.money = money+self.money


print(Worker(name='zhangsan', num=2021001, work_time=50, time=60, money=0))
print(Salesman(name='lisi', num=2021002, sales_volume=50000, proportion=0.1, money=0))
print(Manager(name='wangwu', num=2021003, money=6000))
print(Salesmanager(name='zhaoliu', num=2021004, sales_volume=56230, proportion=0.1, money=1500))