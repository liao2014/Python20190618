# Author:UserA
# socket示例----服务端
# 发一次接收一次版本
import socket

server = socket.socket()
server.bind(("localhost", 1212))#绑定要监听的端口
server.listen()#监听

print("开始等待客户端传递过来的数据")
# conn是客户端连接过来之后在服务端为其生成的一个实例
conn, addr = server.accept()


data = conn.recv(1024)
print("客户端传递过来的数据为：",data)
print("接收到客户端的数据啦")
conn.send(data.upper())
server.close()
