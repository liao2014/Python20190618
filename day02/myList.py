# Author:UserA
names = ["zhangsan", "lisi", "wangwu", "zhaoliu"]
print(names)
print(names[0])
print(names[1:3])  # 切片，不包含最后的值
print(names[-1])  # 取倒数第一个值
print(names[-2])  # 取倒数第二个值
print(names[-3:])  # 取出来倒数第一个到倒数第四个值，但是不包含倒数第四个。反向也是从0开始算。
names.reverse()
print(names)
names.sort()
print(names)
names2 = ["zhangsan", ["lisi", "lisi2"], "wangwu", "zhaoliu"]
names2 = names2.copy()  # copy()浅拷贝,只是拷贝了第一层
#深拷贝deepcopy
