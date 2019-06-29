# Author:UserA
# 线程示例一
import threading
import time

def sayhi(num):  # 定义每个线程要运行的函数
    print("running on number:%s" % num)
    time.sleep(2)

t1 = threading.Thread(target=sayhi, args=("t1",))  # 生成一个线程实例,args第二个参数没有也必须使用逗号分开。
t2 = threading.Thread(target=sayhi, args=(2,))  # 生成另一个线程实例

t1.start()  # 启动线程
t2.start()  # 启动另一个线程

# print(t1.getName())  # 获取线程名
# print(t2.getName())
