# Author:UserA
# 面向对象入门小例子
class Dog:
    num = 11  # 类变量

    # 构造函数，在实例化时候做一些类的初始化工作，例如给实例赋名字，传参数等。
    def __init__(self, name):
        # 实例变量（静态属性），赋给了实例
        # 实例变量的作用域就是实例本身
        self.name = name
        # self.__name = name #私有属性，差别在两个下划线__

    # 类的方法，也就是功能，（动态属性）
    def wangwang(self):
        print("%s : wang wang 叫...." % self.name)

    def __del__(self):
        print("析构函数，程序结束，释放资源")

# 实例化
# d1就是一个实例，也就是一个对象
d1 = Dog("dog1")
d2 = Dog("dog2")
d3 = Dog("dog3")
d1.wangwang()
d2.wangwang()
d3.wangwang()

print(Dog.num)
