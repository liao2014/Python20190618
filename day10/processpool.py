# Author:UserA
# 进程池
from  multiprocessing import Process, Pool
# from  multiprocessing import freeze_support  # 在windows上执行需要导入,使用if __name__ == '__main__'模块测试之后发现不导入也能执行啦。
import time
import os

def Foo(i):
    time.sleep(2)
    print("in process ", os.getpid())
    # print("foo ",i)
    return i + 100

def Bar(arg):
    print('-->exec done:', arg)

if __name__ == '__main__':
    pool = Pool(5)  # 允许进程池里面同时放入5个进程

    for i in range(15):
        pool.apply_async(func=Foo, args=(i,), callback=Bar)  # callback回调
        # pool.apply(func=Foo, args=(i,))
        # pool.apply_async(func=Foo, args=(i,))

    print('end')
    pool.close()
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
