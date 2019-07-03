# Author:UserA
# 进程间通信——进程队列
from multiprocessing import Process, Queue

def f(q):
    q.put([2, None, "HelloWorld"])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())  # prints "[2, None, "HelloWorld"]"
    p.join()
