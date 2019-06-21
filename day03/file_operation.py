# Author:UserA
# 文件操作
# file = open("SongFile", encoding="utf-8").read()
# print(file)

# f是一个文件句柄，也就是文件的内存对象
# r代表读模式
# w代表写模式，指的是新创建一个文件，之后不能读
# r+，可读写文件。可读；可写；可追加
# a : append 表示追加，但是追加之后也不能读
f = open("SongFile", 'r', encoding="utf-8")
# data = f.read()
# print(data)

# write这个会覆盖原来的文件
# f.write("北京北京")
# f.close()
# 按照行读取
# print(f.readline())
# 读取多行
for i in range(5):
    print(f.readline())
# readlines返回的是一个列表
# print(f.readlines())
# for line in f.readlines():
#     print(line.strip())  # 去掉换行。
for line in f:
    print(line)