# Author:UserA
# 守护线程示例：主线程不会等守护线程执行完毕就会直接退出整个程序。
import threading
import time

def run(num):  # 定义每个线程要运行的函数
    print("running on: %s" % num)
    time.sleep(2)
    print("task done ", num, threading.current_thread())

start_time = time.time()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run, args=("t-%s" % i,))  # 生成一个线程实例
    t.setDaemon(True)  # 把当前线程设置为守护线程
    t.start()  # 启动线程
    t_objs.append(t)
print(t_objs)  # t_objs这个存放所有的t线程
# for i in t_objs:
#     t.join()  # 等待每个进程运行完

end_time = time.time()
print("所有进程执行完了", threading.current_thread())
print("花费的时间为：", (end_time - start_time))
