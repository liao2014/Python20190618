# Author:UserA
# 集合测试
list1 = [1, 2, 2, 5, 5, 3]
print(list1, type(list1))  # <class 'list'> 数组
list2 = set(list1)
print(list2, type(list2))  # <class 'set'> 集合
print(list2)

list3 = set([1, 2, 6])
print("list2和list3的交集为：", list2.intersection(list3))
print("list2和list3的并集为：", list2.union(list3))
print("list2中有list3中没有差集：", list2.difference(list3))
print("list3中有list2中没有差集：", list3.difference(list2))
print("list2是不是list3的子集：", list2.issubset(list3))

# 添加单个操作
list2.add(999)
print("增加之后的list2:", list2)
# 添加多项
list3.update([66, 77])
print("增加之后的list3:", list3)
# 判断是不是在集合里面
print("判断1是不是在list3中间", 1 in list3)  # 列表、集合、字符串都是这样写
# 删除,随机删除
# print(list3.pop())
# 删除,指定删除
print(list3.remove(66))
print("删除之后的list3：", list3)
# 计算集合长度
print("list3的长度", len(list3))
