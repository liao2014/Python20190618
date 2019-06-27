# Author:UserA
# 静态方法示例
class Dog(object):
    def __init__(self, name):
        self.name = name

    # staticmethod 实际上和类已经没有什么关系了，和类唯一关联就是通过类名调用了，但是类管不了里面的内容。
    # @staticmethod
    def eat(self, food):
        print("%s eat %s" % (self.name, food))

d = Dog("dog1")
d.eat("包子")
