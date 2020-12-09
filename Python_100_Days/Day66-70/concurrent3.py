# 多进程
import datetime
import time
import multiprocessing


def task(pid):
    time.sleep(0.5)
    print('%s Task %d done.' % (str(datetime.datetime.now()), pid))


def single_thread():
    for i in range(0, 10):
        task(i)


def multi_thread():
    for i in range(0, 10):
        multiprocessing.Process(target=task, args=(i,)).start()


if __name__ == '__main__':
    # single_thread()
    multi_thread()
