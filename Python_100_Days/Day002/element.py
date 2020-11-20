def element_type():
    a = 100
    b = 23.45
    c = 'hello'
    d = True
    e = 1 + 5j

    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))


def element_var():
    a = int(input('a='))
    b = int(input('b='))

    print('%d + %d = %d' % (a, b, a + b))
    print('%d - %d = %d' % (a, b, a - b))
    print('%d * %d = %d' % (a, b, a * b))
    print('%d / %d = %f' % (a, b, a / b))
    print('%d // %d = %d' % (a, b, a // b))
    print('%d %% %d = %d' % (a, b, a % b))
    print('%d ** %d = %d' % (a, b, a ** b))
    print("a=", '123')


def temperature():
    f = float(input('请输入华氏温度='))
    c = (f - 32) / 1.8
    print('%1.f华氏温度=%1.f摄氏温度' % (f, c))


def round():
    r = float(input('输入半径='))
    m = 2 * 3.1416 * r
    n = 3.1416 * r * r
    print('周长=%1.f, 面积=%1.f' % (m, n))


if __name__ == '__main__':
    # element_type()
    # element_var()
    # temperature()
    round()


