class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, name):
        self._name = name


class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self):
        print('%s正在学习%s' % (self._name, self._grade))


class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self):
        print('%s%s正在讲课' % (self._title, self._name))


def main():
    s = Student('Lily', 25, 'History')
    s.study()
    t = Teacher('Lucy', 36, '高级教师')
    t.teach()


if __name__ == '__main__':
    main()
