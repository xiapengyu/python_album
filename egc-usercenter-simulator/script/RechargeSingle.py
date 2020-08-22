"""
模拟用户充值,默认充值99999元
"""

import psycopg2
from constant import Constant
from utils import RechargeUtil

# 创建数据库连接对象
db_config = Constant.DATABASE_ENV_DEV

conn = psycopg2.connect(database=db_config.get("db_name"), user=db_config.get("db_username"),
                        password=db_config.get("db_password"), host=db_config.get("db_host"),
                        port=db_config.get("db_port"))

# 创建指针对象
cur = conn.cursor()
# 执行sql语句
sql = Constant.QUERY_USER_INFO_BY_PHONE.format("15019250605")

print("执行sql:{}".format(sql))
cur.execute(sql)

results = cur.fetchall()
# 结果不为空
if results[0] is not None:
    # 获取用户uuid
    user_uuid = results[0][1]
    # 计算签名
    sign = RechargeUtil.recharge(user_uuid, Constant.DEFAULT_BALANCE)
    # 更新用户余额与签名
    cur.execute(Constant.UPDATE_USER_BALANCE_SQL.format(sign, Constant.DEFAULT_BALANCE, user_uuid))

conn.commit()
cur.close()
conn.close()
