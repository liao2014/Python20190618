# Author:UserA
# 生产者消费者模型

import threading, time
import queue

# q = queue.Queue(maxsize=10)
q = queue.Queue()

def producer(name):
    # count = 0
    # while True:
    for i in range(20):
        q.put("包子 %s" % i)
        # print("生成了包子",count)
        # count += 1
def consumer(name):
    while q.qsize() > 0:
        print("%s 取到 %s " % (name, q.get()))
        time.sleep(1)
        # q.task_done()  # 告知这个任务执行完了

p = threading.Thread(target=producer, args=("zhangsan",))
c = threading.Thread(target=consumer, args=("lisi",))
c2 = threading.Thread(target=consumer, args=("wangwu",))
p.start()
c.start()
c2.start()
'''
import queue
q = queue.Queue(maxsize=10)
for i in range(10):#测试看到 range的参数大于maxsize就死循环，小于等于maxsize就正常输出
    q.put(i)
for i in range(q.qsize()):
    print(q.get())
'''