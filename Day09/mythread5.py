# Author:UserA
# 线程递归锁
import threading, time

def run1():
    print("the first part data")
    lock.acquire()
    global num
    num += 1
    lock.release()
    return num

def run2():
    print("the second part data")
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2

def run3():
    lock.acquire()
    res = run1()
    print('--------between run1 and run2-----')
    res2 = run2()
    lock.release()
    print(res, res2)

if __name__ == '__main__':

    num, num2 = 0, 0
    lock = threading.RLock() #这里要是使用Lock()就会自己给自己锁死，造成死循环
    for i in range(10):
        t = threading.Thread(target=run3)
        t.start()

while threading.active_count() != 1:
    print(threading.active_count())
else:
    print('---all threads done---')
    print(num, num2)
