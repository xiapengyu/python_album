"""
批量用户充值,默认充值99999元
"""

import psycopg2
from constant import Constant
from utils import RechargeUtil

# 创建数据库连接对象
db_config = Constant.DATABASE_ENV_CDT_DEV

conn = psycopg2.connect(database=db_config.get("db_name"), user=db_config.get("db_username"),
                        password=db_config.get("db_password"), host=db_config.get("db_host"),
                        port=db_config.get("db_port"))

# 创建指针对象
cur = conn.cursor()

# 执行sql语句
# sql = Constant.QUERY_TOTAL_USER
sql = "select * from cha.cha_user_info"

print("\n执行sql:{}".format(sql))
cur.execute(sql)

results = cur.fetchall()
# 结果不为空
if results is not None:
    for user in results:
        # 获取用户uuid
        union_id = user[1]
        # 计算签名
        sign = RechargeUtil.recharge(union_id, Constant.DEFAULT_BALANCE)
        # 更新用户余额与签名
        print("更新用户{}余额balance={}, sign={}".format(union_id, Constant.DEFAULT_BALANCE, sign))
        cur.execute(Constant.UPDATE_USER_BALANCE_SQL.format(sign, Constant.DEFAULT_BALANCE, union_id))

    conn.commit()
    cur.close()
    conn.close()
else:
    print("未查询到用户信息")

