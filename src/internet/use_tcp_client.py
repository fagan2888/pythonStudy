import socket

# TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据。

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('127.0.0.1', 9999))
# 接受欢迎消息
print(s.recv(1024).decode('utf-8'))

for data in [b'Michael', b'Tracy', b'Bob', b'Sarah']:
    # 发送数据
    s.send(data)
    print('', s.recv(1024).decode('utf-8'))
# 发送客户端退出命令
s.send(b'exit')
# 关闭连接
s.close()


