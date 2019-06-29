# Author:UserA
# 线程之event示例——红绿灯
import time
import threading

event = threading.Event()

def lighter():
    count = 0
    event.set()
    while True:
        if count > 5 and count <= 10:  # 改成红灯
            event.clear()  # 把标志位清空了
            print('\033[41;1m  red light on  \033[0m')
        elif count > 10:
            event.set()  # 变绿灯
            count = 0
        else:
            print('\033[42;1m  green light on  \033[0m')
        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():
            print("%s running..." % name)
            time.sleep(1)
        else:
            print("%s waiting..." % name)
            event.wait()
            print("%s green ligth on, go go go..." % name)

light = threading.Thread(target=lighter, )
light.start()

car1 = threading.Thread(target=car, args=("BMW",))
car1.start()
