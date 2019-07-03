#Author:UserA
# 协程——greenlet
# greenlet是一个用C实现的协程模块，相比与python自带的yield，它可以在任意函数之间随意切换，不需把这个函数先声明为generator

from greenlet import greenlet

def fun1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()

def fun2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(fun1)
gr2 = greenlet(fun2)
gr1.switch()
# 输出的结果是 12 56 34 78