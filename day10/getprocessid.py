# Author:UserA
# 获取进程id

from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())  # 获取父进程的id
    print('process id:', os.getpid())  # 获取自己的进程id
    print("\n")

def f(name):  # 这个父进程是调用它的进程
    info('\033[31;1m function f \033[0m')
    print('hello', name)

if __name__ == '__main__':  # 这个父进程就是PyCharm的的进程。
    info('\033[32;1m main process line \033[0m')
    p = Process(target=f, args=('zhangsan',))
    p.start()
    p.join()
