def foo():
    global a
    a = 200
    print(a)


def main():
    foo()
    s1 = r'\'hello, world!\''
    s2 = r'\n\\hello, world!\\\n'
    print(s1, s2)
    pass


if __name__ == '__main__':
    main()
