# Author:UserA
# 生成器示例2—通过yield实现在单线程的情况下实现并发运算的效果
import time

def consumer(name):
    print("%s 准备吃包子 " % name)
    while True:
        baozi = yield
        print("包子[%s]来了,被消费者[%s]吃了!" % (baozi, name))

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c3 = consumer('C')
    c.__next__()
    c2.__next__()
    c3.__next__()
    print("生产者开始准备做包子啦!")
    for i in range(3):
        time.sleep(1)
        print("做的第 %s 个包子，被多个消费者分了" % (i + 1))
        c.send(i)
        c2.send(i)
        c3.send(i)

producer("UserA")
