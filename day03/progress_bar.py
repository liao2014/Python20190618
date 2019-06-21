# Author:UserA
# 进度条
import sys, time

for i in range(30):
    sys.stdout.write("#")
    sys.stdout.flush() #刷新到控制台上
    time.sleep(0.2)
