# Author:UserA
# 字典例子
info = {
    'stu1': 'zhangsan',
    'stu2': 'lisi',
    'stu3': 'wangwu'  # 最后一个逗号，写不写不影响运行。
}
print(info)
# 增加
info['stu4'] = 'zhaoliu'
# 查询
print(info['stu1'])
# 删除
info.pop('stu1')
# 修改
info['stu1'] = 'zhangsan666'
print(info)
