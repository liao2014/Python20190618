# Author:UserA
# json反序列化示例
import json

f = open("json_serialize.txt", "r")
data = json.loads(f.read())  # 注意是loads，不是load！！！
print(data)
