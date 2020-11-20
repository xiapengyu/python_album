import math
from random import randint
from Day006 import module1
from Day006 import module2


def fac(m):
    s = 1;
    for i in range(1, m + 1):
        s *= i
    return s


def roll_dice(n=2):
    """摇色子"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c


def add2(*args):
    total = 0
    for val in args:
        total += val
    return total


if __name__ == '__main__':
    print(fac(5))
    print(math.factorial(5))
    # 如果没有指定参数那么使用默认值摇两颗色子
    print(roll_dice())
    # 摇三颗色子
    print(roll_dice(3))
    print(add())
    print(add(1))
    print(add(1, 2))
    print(add(1, 2, 3))
    # 传递参数时可以不按照设定的顺序进行传递
    print(add(c=50, a=100, b=200))
    print('========================')
    print(add2())
    print(add2(1))
    print(add2(1, 2))
    print(add2(1, 2, 3))
    print(add2(1, 3, 5, 7, 9))
    print('========================')
    module1.foo()
    module2.foo()
