# Author:UserA
# 多态示例

class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass

    # 下面使用多态实现二：在父类里面定义多态的通用函数类
    @staticmethod
    def animal_talk(obj):
        obj.talk()

class Cat(Animal):
    def talk(self):
        print("miao miao ...")

class Dog(Animal):
    def talk(self):
        print("wang wang ...")

# d = Dog("dog1")
# d.talk()
# c = Cat("cat1")
# c.talk()
'''
# 下面使用多态实现一：在父类外面定义多态的通用函数类
def animal_talk(obj):
    obj.talk()

d = Dog("dog1")
c = Cat("cat1")
animal_talk(d)
animal_talk(c)
'''
d2 = Dog("dog2")
c2 = Cat("cat2")
# 多态更多的时候是用来进行接口的重用
Animal.animal_talk(d2)
Animal.animal_talk(c2)

