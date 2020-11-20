def auth():
    username = input('请输入用户名:')
    password = input('请输入明码:')

    if username == 'admin' and password == '123456':
        print(True)
    else:
        print(False)


def logic():
    x = float(input('x = '))
    if x > 1:
        y = 3 * x - 5
    elif x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
    print('f(%.2f) = %.2f' % (x, y))


# 计算三角形面积，海伦公式
def rectangle():
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    if a + b > c and a + c > b and b + c > a:
        print('周长: %2.f' % (a + b + c))
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print('面积: %2.f' % (area))
    else:
        print('不能构成三角形')


if __name__ == '__main__':
    # auth()
    # logic()
    rectangle()

