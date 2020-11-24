from abc import abstractmethod


class Pet(object):

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def make_voice(self):
        pass


class Dog(Pet):
    def make_voice(self):
        print("%s汪汪汪" % self._name)


class Cat(Pet):
    def make_voice(self):
        print("%s喵喵喵" % self._name)


def main():
    dog = Dog('旺财')
    dog.make_voice()
    cat = Cat('妙妙')
    cat.make_voice()


if __name__ == '__main__':
    main()