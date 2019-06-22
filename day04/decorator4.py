# Author:UserA
# 装饰器完整示例
import time

# 通过高阶函数+嵌套函数实现装饰器  无参数的例子
def timmer(f):
    def deco():
        start_time = time.time()
        f()
        end_time = time.time()
        print("共计运行时间为：", end_time - start_time)

    return deco

# 通过高阶函数+嵌套函数实现装饰器  有参数的例子
def timmer2(f):
    def deco(*args, **kwargs):
        start_time = time.time()
        f(*args, **kwargs)
        end_time = time.time()
        print("共计运行时间为：", end_time - start_time)

    return deco

# @timmer  # 等价于func1 = timmer(func1)
def func1():
    time.sleep(3)
    print("func1....")

@timmer2  # 等价于func1 = timmer(func1)
def func2(name, age):
    time.sleep(3)
    print("func2....", name, age)

# func1 = timmer(func1)
# func1() #无参数的装饰器测试
func2("liao", 24)  # 有参数的装饰器测试
