from random import randint
from threading import Thread
from time import time, sleep


class DownTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('start to download %s' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s download finished, cost %d s' % (self._filename, time_to_download))


def main():
    start = time()
    t1 = DownTask('Python从入门到住院.pdf')
    t2 = DownTask('Peking Hot.avi')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))


if __name__ == '__main__':
    main()
