# Author:UserA
'''
username = input("请输入用户名：")
password = input("请输入密码：")
print("用户名为：" + username + "，密码为：" + password)
'''
# 下面格式化输出一些信息
name = input("请输入姓名：")
age = input("请输入年龄：")
sal = input("请输入薪水：")
info = '''%s信息如下：\n年龄：%s，薪水：%s''' % (name, age, sal)
print(info)
