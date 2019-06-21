#Author:UserA
# 编辑文件指定的地方的内容，并写到一个新的文件中，或者写会原来的文件中
f = open("SongFile", 'r', encoding="utf-8")
f2 = open("SongFile2", 'w', encoding="utf-8")
for line in f:
    if "当我年少轻狂" in line:
        line = line.replace("当我年少轻狂","当我年少轻狂_f2文件")
    f2.write(line)
f.close()
f2.close()