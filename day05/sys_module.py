#Author:UserA
# sys模块
'''
sys.argv           命令行参数List，第一个元素是程序本身路径
sys.exit(n)        退出程序，正常退出时exit(0)
sys.version        获取Python解释程序的版本信息
sys.maxint         最大的Int值,3.x之后没有这个属性
sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       返回操作系统平台名称
'''
import sys
print(sys.version)
print(sys.path)
print(sys.platform)