# 协程
import datetime
import gevent


def task(pid):
    gevent.sleep(0.5)
    print('%s Task %d done.' % (str(datetime.datetime.now()), pid))


def sync():
    for i in range(0, 10):
        task(i)


def asyn():
    threads = [gevent.spawn(task, i) for i in range(0, 10)]
    gevent.joinall(threads)


if __name__ == '__main__':
    # sync()
    asyn()
