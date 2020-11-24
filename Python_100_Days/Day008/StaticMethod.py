class Triangle(object):

    def __init__(self, a=0, b=0, c=0):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return (a + b) > c and (a + c) > b and (b + c) > a

    def perimeter(self):
        return self._a + self._b + self._c


def main():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
    else:
        print('invalid')


if __name__ == '__main__':
    main()
