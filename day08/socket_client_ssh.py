# Author:UserA
# 使用socket实现ssh——客户端

import socket

client = socket.socket()  # 声明socket类型，同时生成socket连接对象
client.connect(('localhost', 1314))

while True:
    cmd = input("请输入客户端传输数据>>:").strip()
    if len(cmd) == 0: continue
    client.send(cmd.encode("utf-8"))  # 处理中文
    cmd_res_size = client.recv(1024)  # 接收命令结果的长度
    print("命令结果大小为：", cmd_res_size)

    # 下面一行解决粘包问题，在Linux下面测试，在Windows下测试有问题。
    # client.send("解决粘包问题，准备好了接收了".encode("utf-8"))

    received_size = 0  # 接收的大小
    received_data = b""  # 接收的数据
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data)
        received_data += data
    else:
        print("received_size", received_size)
        print("received_data", received_data.decode())
server.close()
