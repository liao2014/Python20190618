# Author:UserA
# 类方法示例
class Dog(object):
    def __init__(self, name):
        self.name = name

    # classmethod 类方法只能访问类变量，不能访问实例变量
    # @classmethod
    def eat(self, food):
        print("%s eat %s" % (self.name, food))

d = Dog("dog1")
d.eat("包子")
