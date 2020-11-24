import re


def reg_phone():
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
        重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
        不是15600998765，也是110或119，王大锤的手机号才是15600998765。
        '''
    list = re.findall(pattern, sentence)
    print(list)
    print('--------华丽的分隔线--------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------华丽的分隔线--------')
    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


def dirty():
    pattern = '[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔'
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub(pattern, '*', sentence, flags=re.IGNORECASE)
    print(purified)  # 你丫是*吗? 我*你大爷的. * you.


def split():
    content = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。';
    lst = re.split(r'[，。, .]', content, flags=re.IGNORECASE)
    while '' in lst:
        lst.remove('')
    print(lst)


def main():
    reg_phone()
    dirty()
    split()


if __name__ == '__main__':
    main()
