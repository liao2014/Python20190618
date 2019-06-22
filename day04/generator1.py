# Author:UserA
# 生成器示例1—斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        # a, b = b, a + b解释如下：
        # t = (b, a + b)  # t是一个tuple
        # a = t[0]
        # b = t[1]
        a, b = b, a + b
        n = n + 1
    return 'done'

# fib(10)
# 上面可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
# 也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        # a, b = b, a + b解释如下：
        # t = (b, a + b)  # t是一个tuple
        # a = t[0]
        # b = t[1]
        a, b = b, a + b
        n = n + 1
    return 'done'

# f2 = fib2(7)
# print(f2)
# print(f2.__next__())
# print(f2.__next__())
f2 = fib2(7)  # 这里测试捕获异常
while True:
    try:
        x = next(f2)
        print('f2:', x)
    except StopIteration as e:
        # 想拿到返回值，需要捕获StopIteration错误，返回值在StopIteration的value中
        print('Generator return value:', e.value)
        break
