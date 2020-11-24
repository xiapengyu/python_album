from random import randint
from threading import Thread
from time import time, sleep


def down_task(filename):
    print('start to download %s' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s download finished, cost %d s' % (filename, time_to_download))


def main():
    start = time()
    t1 = Thread(target=down_task, args=('Python从入门到住院.pdf',))
    t1.start()
    t2 = Thread(target=down_task, args=('Peking Hot.avi',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))


if __name__ == '__main__':
    main()
