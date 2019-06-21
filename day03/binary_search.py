# Author:UserA
# 递归经典案例-二分查找

# 数据列表,测试数据必须有序列表
data = [1, 2, 5, 6, 9, 11, 15, 16, 17, 19]


# data = [1]
# data = []

def binary_search(data, num):
    print(data)

    if len(data) > 1:
        mid = int(len(data) / 2)
        if data[mid] == num:  # 找到数字了
            print("找到数字", data[mid])
        elif data[mid] > num:  # 找的数在mid左边
            print("找的数在 %s 左面" % data[mid])
            return binary_search(data[0:mid], num)
        else:  # 找的数在mid右面
            print("找的数在 %s 右面" % data[mid])
            return binary_search(data[mid + 1:], num)
    elif len(data) == 0:  # 这个判断感觉要不要都行，一般查找也没人设置data为空
        return "测试列表不能为空"
    else:  # 其实这个else里面之后data的长度等于1这一个情况了。
        if data[0] == num:  # 找到数字了
            print("找到数字： ", data[0])
        else:
            print("数字 %s 不在列表里" % num)


binary_search(data, 5)
