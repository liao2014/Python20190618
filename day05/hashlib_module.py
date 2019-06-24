# Author:UserA
# hashlib加密示例
import hashlib

# 下面使用md5模块
m = hashlib.md5()
m.update(b"Hello")
m.update(b"World")
print(m.digest())
print(m.hexdigest())  # 16进制格式hash
print(len(m.hexdigest()))  # 16进制格式hash

m2 = hashlib.md5()
m2.update(b"HelloWorld")
print("m2:  ", m.hexdigest())
print("m2哈希的长度:  ", len(m.hexdigest()))

# 下面使用sha模块
# hash = hashlib.sha1()
# hash.update(b'HelloWorld')
# print(hash.hexdigest())

hash2 = hashlib.sha256()
hash2.update(b'HelloWorld')  # b代表的是二进制数据。
print(hash2.hexdigest())
print(len(hash2.hexdigest()))
