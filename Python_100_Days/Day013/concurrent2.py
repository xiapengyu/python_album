from time import time, sleep
from random import randint
from multiprocessing import Process
from os import getpid


def down_task(filename):
    print('start to download %s, process id is %s' % (filename, getpid()))
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s download finished, cost %d s' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=down_task, args=('Python从入门到住院.pdf',))
    p1.start()
    p2 = Process(target=down_task, args=('Peking Hot.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('total cost %.2f s' % (end - start))


if __name__ == '__main__':
    main()
