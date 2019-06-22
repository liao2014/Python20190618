#Author:UserA
# 装饰器示例二
# Python先声明再调用，解释器会在调用之前会将代码解释到内存中。
# 下面的可以正常运行
def foo():
    print("foo.....")
    bar()
def bar():
    print("bar.....")
foo()

# 下面的可以正常运行
# def bar():
#     print("bar.....")
# def foo():
#     print("foo.....")
#     bar()
# foo()

# 下面的不可运行，提醒找不到bar()
# def foo():
#     print("foo.....")
#     bar()
# foo()
# def bar():
#     print("bar.....")
