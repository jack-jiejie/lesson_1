__author__ = "yin"
__data__ = "2020/4/4 23:00"

class Person():
    pass

# p = Person()
# print(type(p))

class Sleep():
    def __init__(self):
        print("构造函数运行......")
    def __new__(cls, *args, **kwargs):
        print("__new__方法运行")
        return Dog()

    def __del__(self):
        print("析构函数运行.....")

class Dog():
    def run(self):
        print("dog run")

# sleep = Sleep()
# print(type(sleep))
# sleep.run()


# 类的动态创建

def get_class(name):
    if name == "dog":
        class Dog():
            def run(self):
                print("dog run")
        return Dog
    else:
        class Cat():
            def run(self):
                print("cat run")
        return Cat

# d = get_class("dog")
# print(d)
# print(type(d))
# d.run(d)

# 使用type动态创建类, ()里面写继承，  {}里面写的是属性
Person2 = type("Person2", (), {"name":"张三"})
print(Person2)
p2 = Person2()
# print(p2.name)


# type动态创建类， 在{}中加入方法
def person3_run(self):
    print("person3 run")

Person3 = type("Person3", (Person2,), {"person3_run":person3_run})
p3 = Person3()
p3.person3_run()
