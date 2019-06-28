# Author:UserA
# 使用socket实现ssh——服务端
import socket, os

server = socket.socket()
server.bind(("localhost", 1314))
server.listen()
while True:
    conn, addr = server.accept()
    print("新的连接：", addr)
    while True:
        print("等待新数据")
        data = conn.recv(1024)
        if not data:
            print("客户端已经断开")
            break
        print("执行指令", data)
        cmd_res = os.popen(data.decode()).read()  # 接收的是字符串，执行的结果也是字符串
        print("before send", len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = "cmd 命令没有返回值"
        conn.send(str(len(cmd_res.encode())).encode("utf-8"))  # cmd_res.encode()是为了解决中文传递中接收和发送大小不一致问题。
        # time.sleep(0.5) #sleep0.5秒刷新 解决粘包初步方法
        # client_ack = conn.recv(1024) #等待客户端确认。  这行代码解决粘包问题，在Windows下面测试不出来粘包问题。
        conn.send(cmd_res.encode("utf-8"))
        print("after send")
server.close()
