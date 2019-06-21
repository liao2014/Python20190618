# Author:UserA
# 函数测试

# 函数
def func1():
    print("func1中间")
    return 1


# 过程
def func2():
    print("func2 中间")


# 下面调用函数和过程
x = func1()
y = func2()
print("x===", x)  # 返回1
print("y===", y)  # 返回None
