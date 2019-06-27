#Author:UserA
# socket示例3——客户端
# 执行客户端传递过来的命令版本
import socket

client = socket.socket()  # 声明socket类型，同时生成socket连接对象
client.connect(('localhost', 1313))

while True:
    msg = input("请输入客户端传输数据>>:").strip()
    if len(msg) == 0: continue
    client.send(msg.encode("utf-8"))  # 处理中文
    data = client.recv(10240)
    print("recv:", data.decode())

client.close()
