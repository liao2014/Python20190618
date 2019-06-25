# Author:UserA
# 继承顺序问题
'''
在Python2中，经典类是按照深度优先来继承的，新式类是按照广度优先继承的。
在Python3中，经典类和新式类都是按照广度优先来继承的。
'''
class A:
    def __init__(self):
        print("A")

class B(A):
    pass
    # def __init__(self):
    #     print("B")

class C(A):
    def __init__(self):
        print("C")

class D(B, C):
    pass
    # def __init__(self):
        # print("D")

# 实例化
# 执行的顺序是 D B C A ,符合广度优先搜索规则
d = D()
