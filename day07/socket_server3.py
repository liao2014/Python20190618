# Author:UserA
# socket示例3——服务端
# 执行客户端传递过来的命令版本
import socket
import os
server = socket.socket()
server.bind(('localhost', 1313))  # 绑定要监听端口
server.listen(5)  # 监听，最多同时打开5个客户端进行排队传数据

print("开始等待客户端传递过来的数据")
while True:
    conn, addr = server.accept()  # 等电话打进来
    # conn就是客户端连过来而在服务器端为其生成的一个连接实例
    print(conn, addr)
    print("客户端传数据准备来了")
    count = 0
    while True:
        data = conn.recv(1024)
        print("recv:", data.decode())
        if not data:
            print("client has lost...")
            break
        # os.popen()是执行命令
        res = os.popen(data.decode()).read() #data.decode()是将data的bytes类型转化为str类型
        conn.send(res.encode("utf-8")) #res.encode("utf-8") 是将res的str类型转bytes
        # count += 1
        # if count > 10: break

server.close()
