# Author:UserA
# socket示例1----客户端
# 发一次接收一次版本
import socket

client = socket.socket()
client.connect(("localhost", 1212))
client.send(b"Hello World")
data = client.recv(1024)
print("客户端接收的返回的数据为：", data)
client.close()
