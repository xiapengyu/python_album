class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s未满十八岁，只能看喜羊羊' % self.name)
        else:
            print('%s已满十八岁，可以看R级片' % self.name)


def main():
    student = Student('Tom', 25)
    student.study('面向对象编程思想')
    student.watch_movie()
    student2 = Student('Lily', 15)
    student2.study('思想品德')
    student2.watch_movie()


if __name__ == '__main__':
    main()
