# Author:UserA
import getpass

# 密码输入密文测试
# 下面的方式在PyCharm中没法测试，要在Windows的cmd窗口中测试才有效。
username = input("请输入用户名：")
password = getpass.getpass("请输入密码：")
print(username, password)
