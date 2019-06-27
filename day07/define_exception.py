#Author:UserA
# 自定义异常示例

class UserAException(Exception):
    def __init__(self, msg):
        self.message = msg

    # 下面的不写也可以
    # def __str__(self):
    #     return self.message

try:
    raise UserAException('自定义异常的内容')
except UserAException as e:
    print(e)
