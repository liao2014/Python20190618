# Author:UserA
# 队列示例  py文件命名的时候千万不能使用queue这种关键字
'''
class queue.Queue(maxsize=0) #先入先出
class queue.LifoQueue(maxsize=0) #last in fisrt out  后进先出
class queue.PriorityQueue(maxsize=0) #存储数据时可设置优先级的队列
'''
import queue

# q = queue.Queue()
q2 = queue.LifoQueue()
q3 = queue.PriorityQueue()
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())
# print(q.get())
# print(q.get())

for i in range(5):
    q2.put(i)
size = q2.qsize()
print("size:", size)
for i in range(size):
    print(q2.get())  # 后进先出

q3.put((1, "zhangsan"))
q3.put((5, "lisi"))
q3.put((3, "wangwu"))
q3.put((2, "zhaoliu"))
for i in range(q3.qsize()):
    print(q3.get())  # 按照优先级排队输出
