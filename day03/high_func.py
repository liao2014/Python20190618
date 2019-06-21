# Author:UserA
# 高阶函数测试
def add(x, y, f):
    return f(x) + f(y)


res = add(3, -6, abs)
print(res)  # 返回值是9
