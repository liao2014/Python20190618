# Author:UserA
# json序列化示例
import json

info = {
    'name': 'liao',
    'age': 25
}
f = open("json_serialize.txt", "w")
f.write(json.dumps(info))
f.close()
