from time import time, sleep
from random import randint


def down_task(filename):
    print('start to download %s' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s download finished, cost %d s' % (filename, time_to_download))


def main():
    start = time()
    down_task('Java Effective')
    down_task('Python Study')
    end = time()
    print('total cost %.2f s' % (end - start))


if __name__ == '__main__':
    main()
