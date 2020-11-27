import random

ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_random_code(length):
    """获取随机验证码"""
    return ''.join(random.choices(ALL_CHARS, k=length))


def main():
    print(get_random_code(4))


if __name__ == '__main__':
    main()
