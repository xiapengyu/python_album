from socket import socket, AF_INET, SOCK_STREAM


def main():
    client = socket()
    client.connect(('127.0.0.1', 20011))
    send_msg = 'hello'
    print('客户端发送消息: %s' % send_msg)
    client.send('hello'.encode('utf-8'))

    recv_msg = client.recv(1024).decode('utf-8')
    print('客户端接收消息: %s' % recv_msg)
    client.close()


if __name__ == '__main__':
    main()
