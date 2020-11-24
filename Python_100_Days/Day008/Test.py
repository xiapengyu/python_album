class Test(object):
    def __init__(self, name):
        self.__name = name

    def __foo(self):
        print(self.__name)


def main():
    test = Test('Hello')
    test.__foo()  # AttributeError: 'Test' object has no attribute '__foo'
    # test._Test__foo()


if __name__ == '__main__':
    main()
