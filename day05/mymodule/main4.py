# Author:UserA
# 导入模块module2测试
import sys, os

print(sys.path)
x = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(x)
sys.path.append(x)
import module2

print(module2.name)
module2.hello()
