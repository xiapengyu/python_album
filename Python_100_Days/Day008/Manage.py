from abc import abstractmethod, ABCMeta


class Employ(object, metaclass=ABCMeta):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employ):

    def get_salary(self):
        return 15000.0


class Programmer(Employ):

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return 150 * self._working_hour


class Saller(Employ):
    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales

    def get_salary(self):
        return 1200.0 + self._sales * 0.05


def main():
    emps = [Manager('曹操'), Manager('刘备'), Manager('孙权'), Programmer('赵云'), Saller('鲁肃')]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hour = int(input('请输入%s本月工作时间: ' % emp.name))
        elif isinstance(emp, Saller):
            emp.sales = float(input('请输入%s本月销售额: ' % emp.name))
        print("%s本月工资为%.2f" % (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()
