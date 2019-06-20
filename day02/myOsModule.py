# Author:UserA
import os

# res1 = os.system("dir")  # 执行命令，不保存结果
res2 = os.popen("dir").read()  # 执行命令，并且会保存结果
print("=====>", res2)
