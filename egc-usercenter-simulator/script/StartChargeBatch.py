"""
用户批量登录与启动充电
"""

import time
from utils import SmartchargeUtil
from constant import Constant

success_list = []
fail_list = []


# 轮询配置的用户数据，用户依次登录并启动充电
for item in Constant.config_data:
    # 解析参数
    phone = item.get("phone")
    pwd = item.get("password")
    device_no = item.get("device_no")
    print("\n批量登录并启动充电,手机号{},密码{},设备编号{}".format(phone, pwd, device_no))

    # 登录并获取用户token
    access_token = SmartchargeUtil.user_login(phone, pwd)
    if str(access_token) != "":
        # 登录成功之后启动充电
        start_result = SmartchargeUtil.start_charge(phone, access_token, device_no)
        if str(start_result) == "success":
            success_list.append(phone)
            # 启动充电成功之后等待10秒钟，再执行下一个用户的登录充电操作
            time.sleep(10)
        else:
            fail_list.append(phone)
            # 启动充电失败，执行下一个用户的登录充电操作
            continue
    else:
        fail_list.append(phone)
        print("获取token失败")
        continue

print("成功的用户{}\n失败的用户{}".format(success_list, fail_list))

