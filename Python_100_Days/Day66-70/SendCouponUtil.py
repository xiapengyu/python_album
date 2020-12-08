"""
充电通赠送电子券工具，设置需要赠送的用户信息与电子券数量，执行脚本输出sql语句，将sql语句在navicate中执行即可
"""
import random
import time

# 需要赠送代金券的用户信息手机号和unionId
user_info = {
    "18666292697": "BEBD55ABD078008056F9E7D0782E5686"
}


def send_type_1(num):
    """
    赠送满2减2代金券
    :param num: 赠送代金券的数量
    :return:
    """
    sql = "INSERT INTO cha.act_coupon_usage_record VALUES ({0}, {1}, 'DZQMJ20201117001', '满2减2充电劵'," \
          " 'YHHD20201113006', {2}, {3}, NULL, '2020-11-16 00:00:00', 'WEIXIN2020111410354328661', NULL," \
          " 5, 1, '2020-11-14 10:35:54', 'SYSTEM_DEFAULT', '2020-11-15 00:00:00', 'admin', 1, " \
          "'2021-12-30 23:59:59', 1, NULL, 0, NULL, NULL, 0, '', '2020-11-17 00:00:00');"
    for key in user_info:
        phone = key
        union_id = user_info[key]
        for index in range(0, num):
            s = create_sql(phone, union_id, sql)
            print(s)


def send_type_2(num):
    """
    赠送满5减5代金券
    :param num: 赠送代金券的数量
    :return:
    """
    sql = "INSERT INTO cha.act_coupon_usage_record VALUES ({0}, {1}, 'DZQMJ20201117002', '满5减5充电劵'," \
          " 'YHHD20201113006', {2}, {3}, NULL, '2020-11-16 00:00:00', 'WEIXIN2020111410354328661', NULL," \
          " 5, 1, '2020-11-14 10:35:54', 'SYSTEM_DEFAULT', '2020-11-15 00:00:00', 'admin', 1, " \
          "'2021-12-30 23:59:59', 1, NULL, 0, NULL, NULL, 0, '', '2020-11-17 00:00:00');"
    for key in user_info:
        phone = key
        union_id = user_info[key]
        for index in range(0, num):
            s = create_sql(phone, union_id, sql)
            print(s)


def send_type_3(num):
    """
    赠送满10减10代金券
    :param num: 赠送代金券的数量
    :return:
    """
    sql = "INSERT INTO cha.act_coupon_usage_record VALUES ({0}, {1}, 'DZQMJ20201117003', '满10减10充电劵'," \
          " 'YHHD20201113006', {2}, {3}, NULL, '2020-11-16 00:00:00', 'WEIXIN2020111410354328661', NULL," \
          " 5, 1, '2020-11-14 10:35:54', 'SYSTEM_DEFAULT', '2020-11-15 00:00:00', 'admin', 1, " \
          "'2021-12-30 23:59:59', 1, NULL, 0, NULL, NULL, 0, '', '2020-11-17 00:00:00');"
    for key in user_info:
        phone = key
        union_id = user_info[key]
        for index in range(0, num):
            s = create_sql(phone, union_id, sql)
            print(s)


def create_sql(phone, union_id, sql):
    """
    构造赠送电子券sql语句
    :param phone:
    :param union_id:
    :param sql: 原始sql
    :return:
    """
    uuid = create_uuid()
    coupon_no = create_coupon()
    return sql.format("'" + uuid + "'", "'" + coupon_no + "'", "'" + union_id + "'", "'" + phone + "'")


def create_uuid():
    """
    随机生成代金券uuid
    :return:
    """
    return time.strftime('%Y%m%d%H%M%S') + '0' + str(random.randint(000000000, 1000000000))


def create_coupon():
    """
    随机生成9位代金券编码
    :return:
    """
    code = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    coupon_no = ''
    for _ in range(1, 10):
        coupon_no += random.choice(code)
    return coupon_no


def main():
    send_type_1(1)
    send_type_2(1)
    send_type_3(1)


if __name__ == '__main__':
    main()
