#Author:UserA
# 进程锁——主要控制输出打印
from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(5):
        Process(target=f, args=(lock, num)).start()