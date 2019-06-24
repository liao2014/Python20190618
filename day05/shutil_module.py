#Author:UserA
# shutil模块
'''
shutil.copyfileobj(fsrc, fdst[, length])
将文件内容拷贝到另一个文件中，可以部分内容

shutil.copyfile(src, dst)
拷贝文件

shutil.copymode(src, dst)
仅拷贝权限。内容、组、用户均不变

shutil.copystat(src, dst)
拷贝状态的信息，包括：mode bits, atime, mtime, flags

shutil.copy(src, dst)
拷贝文件和权限

shutil.copy2(src, dst)
拷贝文件和状态信息
'''