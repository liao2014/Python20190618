# Author:UserA
# 异常处理示例

names = ["zhangsan", "lisi"]
data = {"name": "zhangsan", "age": 25}

'''
# 方法一：针对每个错误单独写
try:
    names[3]
    data['address']
except KeyError as e:
    print("没有这个key：", e)
except IndexError as e:
    print("下表越界：", e)
'''
'''
# 方法二：给异常放到一起
try:
    names[3]
    data['address']
except (KeyError,IndexError) as e:
    print("出错了：", e)
'''
'''
# 方法三：统一使用
try:
    # names[3]
    data['address']
except Exception as e:
    print("出错啦：", e)
'''
'''
# 当出现未知错误时候的处理方式
try:
    # names[3]
    # data['address']
    open("aa.txt")
except (KeyError, IndexError) as e:
    print("出错了：", e)
except Exception as e:
    print("未知错误是：", e)
'''

# else 是程序没有错误的时候执行，finally是不管有没有错误，都执行。
try:
    # names[3]
    # data['address']
    # open("aa.txt")
    a = 100
except (KeyError, IndexError) as e:
    print("出错了：", e)
except Exception as e:
    print("未知错误是：", e)
else:
    print("程序没有错误，执行这里的")
finally:
    print("不管有没有错误，都要执行这里的代码")
