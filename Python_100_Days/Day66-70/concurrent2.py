# 多线程
import datetime
import threading
import time


def task(pid):
    time.sleep(0.5)
    print("%s Task %d done." % (str(datetime.datetime.now()), pid))


def single_thread():
    for i in range(0, 10):
        task(i)


def multi_thread():
    for i in range(0, 10):
        threading.Thread(target=task, args=(i,)).start()


if __name__ == '__main__':
    # single_thread()
    multi_thread()
