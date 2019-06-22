#Author:UserA
# 装饰器-嵌套函数示例
def foo():
    print("foo.....")
    def bar():
        print("bar.....")
    bar()
foo()