import pymysql


class User(object):

    def __init__(self, name, age, job, phone):
        self._name = name
        self._age = age
        self._job = job
        self._phone = phone

    def name(self):
        return self._name

    def age(self):
        return self._age

    def job(self):
        return self._job

    def phone(self):
        return self._phone


def get_conn():
    """
    说明：如果不希望每次SQL操作之后手动提交或回滚事务，可以像上面的代码那样，在创建连接的时候多加一个名为`autocommit`的参数并将它的值设置为`True`，
    表示每次执行SQL之后自动提交。如果程序中不需要使用事务环境也不希望手动的提交或回滚就可以这么做。
    """
    con = pymysql.connect(host='127.0.0.1', port=3306,
                          database='spring_test', charset='utf8',
                          user='root', password='xia4698083', autocommit=True)
    return con


def get_list():
    con = get_conn()
    try:
        # 2. 通过连接对象获取游标
        with con.cursor() as cursor:
            # 3. 通过游标执行SQL并获得执行结果
            cursor.execute("select * from user")
            results = cursor.fetchall()
        for item in results:
            print(item)
    finally:
        # 5. 关闭连接释放资源
        con.close()


def add_user(user):
    # 1. 创建数据库连接对象
    con = get_conn()
    try:
        # 2. 通过连接对象获取游标
        with con.cursor() as cursor:
            # 3. 通过游标执行SQL并获得执行结果
            result = cursor.execute(
                "insert into user (user_name, age, job, phone) values (%s, %s, %s, %s)",
                (user.name(), user.age(), user.job(), user.phone())
            )
        if result == 1:
            print('添加成功!')
        # 4. 操作成功提交事务
        con.commit()
    finally:
        # 5. 关闭连接释放资源
        con.close()


def del_user(key):
    # 1. 创建数据库连接对象
    con = get_conn()
    try:
        # 2. 通过连接对象获取游标
        with con.cursor() as cursor:
            # 3. 通过游标执行SQL并获得执行结果
            result = cursor.execute(
                "delete from user where id = (%s)", (key,)
            )
        if result == 1:
            print('删除成功!')
        # 4. 操作成功提交事务
        con.commit()
    finally:
        # 5. 关闭连接释放资源
        con.close()


def main():
    # user = User('Leo', 29, 'Killer', '15548790')
    # add_user(user)
    # del_user(14)
    get_list()


if __name__ == '__main__':
    main()
