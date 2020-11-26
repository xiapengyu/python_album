from socket import socket, AF_INET, SOCK_STREAM
from datetime import datetime


def main():
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('127.0.0.1', 20011))
    server.listen(512)
    print('服务器开始监听......')
    while True:
        client, address = server.accept()
        print(str(address) + '连接到服务器......')

        recv_msg = client.recv(1024).decode('utf-8')
        print('服务端接收消息: %s' % recv_msg)

        client.send(str(datetime.now()).encode('utf-8'))
        client.close()


if __name__ == '__main__':
    main()

