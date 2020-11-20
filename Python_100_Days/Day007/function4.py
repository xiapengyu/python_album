import os
import time
from random import randint


def mar_queue():
    """
    模拟跑马灯打印字符串
    :return:
    """
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出，linux系统使用os.system('clear')，windows系统使用os.system('cls')
        os.system('cls')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


def generate_code(code_len=4):
    """
    生成指定长度的验证码
    :param code_len:验证码的长度(默认4个字符)
    :return:由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for _ in range(0, code_len):
        index = randint(0, len(all_chars) - 1)
        code += all_chars[index]
    print(code)
    return code


def get_suffix(filename='', has_pot=False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_pot else pos - 1
        return filename[index:]
    else:
        return ''


def yh_tangle():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


def main():
    yh_tangle()
    # generate_code()
    # mar_queue()


if __name__ == '__main__':
    main()
