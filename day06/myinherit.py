# Author:UserA
# 继承示例

# class Person: # 经典类
class Person(object):  # 新式类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s eat......" % self.name)

    def sleep(self):
        print("%s sleep......" % self.name)

    def talk(self):
        print("%s   talk......" % self.name)

# 继承方式如下
class Man(Person):
    # 在子类中针对父类中的函数加上新的功能
    def __init__(self, name, age, money):
        # Person.__init__(self, name, age)
        # 下面的这个代码和上面一样作用
        super(Man, self).__init__(name, age)
        self.money = money

    # 子类中独有方法
    def drink(self):
        print("%s drink...... 在Man子类中" % self.name)

        # 子类覆盖父类方法
        # def talk(self):
        #     print("%s   talk...... 子类中 " % self.name)

# m1 = Man("zhangsan", 22)
# m1.eat()
# m1.sleep()
# m1.talk()
# m1.drink()
m2 = Man("zhangsan", 22, 10000)
m2.eat()
m2.sleep()
m2.talk()
m2.drink()
print(m2.money)
