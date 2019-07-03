#Author:UserA
# 协程——gevent
'''
Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，
在gevent中用到的主要模式是Greenlet, 它是以C扩展模块形式接入Python的轻量级协程。 
Greenlet全部运行在主程序操作系统进程的内部，它们被协作式地调度。
'''

import gevent

def func1():
    print('func1  111')
    gevent.sleep(3)
    print('func1  222')

def func2():
    print('func2  333')
    gevent.sleep(2)
    print('func2  444')

def func3():
    print('func3  555')
    gevent.sleep(1)
    print('func3  666')

gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    gevent.spawn(func3),
])