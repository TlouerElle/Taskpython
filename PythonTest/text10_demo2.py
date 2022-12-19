class Person:
    count = 0

    def __init__(self, name, age):
        Person.count += 1
        self.name = name
        self.age = age

    @classmethod
    def count_object(cls):
        cls.count += 1
        return cls.count


p1 = Person('zhangsn', 18)
p2 = Person('lisi', 19)
p3 = Person('zhaoliu', 21)
p4 = Person('wangwu', 20)

print('创建了', Person.count_object(), '个对象')
