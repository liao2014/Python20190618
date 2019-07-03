# Author:UserA
# 多进程
import multiprocessing
import time

def run(name):
    time.sleep(2)
    print("hello ", name)

if __name__ == '__main__':  # 表示需要自己主动执行的程序。当导入这个文件的时候，这些代码不会执行。
    # 10个进程一共也就执行2秒左右，也就是实现了多进程
    for i in range(10):
        p = multiprocessing.Process(target=run, args=("UserA %i" % i,))
        p.start()
