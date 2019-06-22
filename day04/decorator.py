# Author:UserA
# 装饰器示例一
import time


def timmer(f):
    def warpper(*args, **kwargs):
        start_time = time.time()
        f()
        end_time = time.time()
        print("fun1()函数运行时间为 %s" % (end_time - start_time))

    return warpper

@timmer
def fun1():
    time.sleep(3)
    print("deco_test1")


fun1()
