from socket import socket, SOCK_STREAM, AF_INET
from threading import Thread
from json import dumps
from base64 import b64encode


def main():
    # 自定义线程类
    class DataHandler(Thread):
        def __init__(self, cclient, data):
            super().__init__()
            self.cclient = cclient
            self.data = data

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'phone101.txt'
            # JSON是纯文本不能携带二进制数据
            # 所以图片的二进制数据要处理成base64编码
            my_dict['filedata'] = self.data
            # 通过dumps函数将字典处理成JSON字符串
            json_str = dumps(my_dict)
            # 发送JSON字符串
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('127.0.0.1', 6789))
    server.listen(512)
    print('服务器启动开始监听...')
    with open('D:\\logs2\\phone101.txt', 'rb') as f:
        # 将二进制数据处理成base64再解码成字符串
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器.')
        # 启动一个线程来处理客户端的请求
        DataHandler(client, data).start()


if __name__ == '__main__':
    main()

