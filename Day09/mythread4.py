# Author:UserA
# 线程锁
import threading
import time

lock = threading.Lock()  # 线程锁,加完之后程序执行编程串行执行了。

def run(n):  # 定义每个线程要运行的函数
    lock.acquire()
    global num
    num += 1
    time.sleep(1)
    # print("n", n)
    lock.release()

num = 0
t_objs = []
for i in range(50):
    t = threading.Thread(target=run, args=("t-%s" % i,))  # 生成一个线程实例
    t.start()  # 启动线程
    t_objs.append(t)
print(t_objs)  # t_objs这个存放所有的t线程
for i in t_objs:
    t.join()  # 等待每个进程运行完

print("所有进程执行完了", threading.current_thread())
print("num:", num)
