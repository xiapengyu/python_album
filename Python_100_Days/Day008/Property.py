class Property(object):
    # 限定对象只能绑定_name, _age属性
    __slots__ = ('_name', '_age')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    @name.setter
    def name(self, name):
        self._name = name

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    p = Property('王大锤', 12)
    p.play()
    p.age = 22
    p.play()
    p.gender = 'M'  # AttributeError: 'Property' object has no attribute 'gender'


if __name__ == '__main__':
    main()
