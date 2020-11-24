from time import sleep
import json

def read_file(path):
    file = None
    try:
        file = open(path, 'r')
        print(file.read())
    except FileNotFoundError:
        print('系统内部错误!')
    finally:
        if file:
            file.close()


def read_file_2(path):
    # 一次读取所有内容
    with open(path, 'r') as f:
        print(f.read())
    print()

    # 逐行读取文件内容
    with open(path, 'r') as f:
        for line in f:
            print(line, end='\n')
            sleep(0.5)
    print()

    # 读取文件逐行读取到列表中
    with open(path, 'r') as f:
        lines = f.readlines()
    print(lines)


def write_file(path):
    file = None
    try:
        # 截断以前的内容，写入新内容
        # file = open(path, 'w')
        # 文件已经存在会产生异常
        # file = open(path, 'x')
        # 追加新内容
        file = open(path, 'a')
        # write()参数是一个字符串
        file.write('恒大智慧充电科技\n')
        # writelines()参数既可以传入字符串又可以传入一个字符序列(如字符串集合)
        file.writelines('房车宝\n')
    except FileNotFoundError:
        print('系统内部错误!')
    finally:
        if file:
            file.close()


def write_json(path):
    my_dict = {
        'name': 'Kasonn',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(my_dict, f)
    except IOError as e:
        print(e)


def main():
    # write_file('D:\\logs2\\content.txt')
    # read_file('D:\\logs2\\content.txt')
    # read_file_2('D:\\logs2\\content.txt')
    write_json('D:\\logs2\\content2.txt')


if __name__ == '__main__':
    main()


# - `dump` - 将Python对象按照JSON格式序列化到文件中
# - `dumps` - 将Python对象处理成JSON格式的字符串
# - `load` - 将文件中的JSON数据反序列化成对象
# - `loads` - 将字符串的内容反序列化成Python对象
