# Author:UserA
# 字符串相关常用函数
str = "my name is UserA"
print(str.capitalize())  # 整个字符串第一个字母大写，并不是指每个单词。
print(str.count("a"))  # 统计a出现次数，区分大小写。
print(str.find("name"))  # 找到name首次出现的位置。
str2 = "my name is {name}"
print(str2.format(name='zhangsan'))
print("2str_33".isidentifier())  # 判断是不是一个合法的变量名
print('+'.join(['1', '2', '3']))  # 返回的结果是： 1+2+3
print('\nzhangsan \nlisi')  # \n回车换行
