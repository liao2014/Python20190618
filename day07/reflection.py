# Author:UserA
# 反射示例：通过字符串映射或修改程序运行时的状态、属性、方法
class Foo(object):
    def __init__(self):
        self.name = "zhangsan"

    def func(self):
        return "func"

obj = Foo()

# 检查是否含有成员
print(hasattr(obj, 'name'))
print(hasattr(obj, 'func'))

# 获取成员
print(getattr(obj, 'name'))
print(getattr(obj, 'func')())  # 这个需要通过()获取数值

# 设置成员
setattr(obj, 'age', 18)
# setattr(obj, 'show', lambda num: num + 1)

# 删除成员
# delattr(obj, 'name')
# delattr(obj, 'func')
