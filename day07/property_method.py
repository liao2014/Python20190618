#Author:UserA
# 属性方法示例
class Dog(object):
    def __init__(self, name):
        self.name = name

    #property把一个方法变成一个静态属性
    @property
    def eat(self):
        print("%s eat %s" % (self.name,"食物"))

d = Dog("dog1")
d.eat
