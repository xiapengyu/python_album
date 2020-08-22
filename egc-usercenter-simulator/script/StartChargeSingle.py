"""
单个用户登录与启动充电
"""

from utils import SmartchargeUtil

user_info = {"phone": "13700000131", "password": "q1234567", "device_no": "11548037"}

# 解析参数
phone = user_info.get("phone")
pwd = user_info.get("password")
device_no = user_info.get("device_no")
print("\n登录并启动充电,手机号{},密码{},设备编号{}".format(phone, pwd, device_no))

# 登录并获取用户token
access_token = SmartchargeUtil.user_login(phone, pwd)
if str(access_token) != "":
    # 登录成功之后启动充电
    start_result = SmartchargeUtil.start_charge(phone, access_token, device_no)
    if str(start_result) == "success":
        print("启动充电成功")
    else:
        print("启动充电失败")
else:
    print("获取token失败")
