"""
单个用户登录并停止充电
"""

from utils import SmartchargeUtil

user_info = {"phone": "13700000131", "password": "q1234567"}

# 解析参数
phone = user_info.get("phone")
pwd = user_info.get("password")
print("\n登录并停止充电,手机号{},密码{}".format(phone, pwd))

# 登录并获取用户token
access_token = SmartchargeUtil.user_login(phone, pwd)
if str(access_token) != "":
    # 登录成功之后停止充电
    stop_result = SmartchargeUtil.stop_charge(access_token)
    if str(stop_result) == "success":
        print("停止充电成功")
    else:
        print("停止充电失败")
else:
    print("获取token失败")
