# Author:UserA
# 通过随机数实现验证码
import random

checkcode = ''
for i in range(4):
    current = random.randrange(0, 4)
    if current != i:  # 这个概率每次只有25%，所以输出的结果里面平均情况下，字母比数字多
        tempcode = chr(random.randint(65, 90))
    else:
        tempcode = random.randint(0, 9)  # 两侧都是闭区间
    checkcode += str(tempcode)
print(checkcode)
