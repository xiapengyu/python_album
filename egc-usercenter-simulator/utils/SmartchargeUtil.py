"""
模拟智慧充电工具
"""

import json
import uuid
from hashlib import md5

import requests

from constant import Constant

"""
用户登录
参数 phone 登录手机号  password 登录密码
返回用户登录凭证
"""


def user_login(phone, password):
    request_url = "http://39.108.167.253/egc-cloudapicomponent/admin/login"
    # request_url = Constant.CHARGE_DOMAIN_TEST + Constant.USER_LOGIN_URL
    password = md5(password.encode('utf-8')).hexdigest()
    headers = {"FrontType": "egc-mobile-ui", "Content-Type": "application/x-www-form-urlencoded",
               "traceId": str(uuid.uuid4()).replace("-", "")}
    body = {"username": phone, "password": password}
    response = requests.post(request_url, data=body, headers=headers)
    if response.status_code == 200:
        result = json.loads(response.text)
        if result.get("code") == "00000":
            token = result.get("data").get("token")
            print("用户{}登陆成功\nToken：{}".format(phone, token))
            return token
        else:
            print("用户{}登陆失败".format(phone))
            return ""
    else:
        print("登陆失败，返回结果：{}".format(response.text))
        return ""


"""
查询用户信息
参数 token 用户登录的凭证
返回用户基本信息(余额，订单号，8位设备编码)
"""


def query_user_info(token):
    request_url = "http://39.108.167.253/egc-cloudapicomponent/api/userAccount/getChargingAccountInfo"
    # request_url = Constant.CHARGE_DOMAIN_TEST + Constant.QUERY_USER_INFO_URL
    headers = {"FrontType": "egc-mobile-ui", "Content-Type": "application/json",
               "traceId": str(uuid.uuid4()).replace("-", ""), "Authorization": token}
    body = {}
    response = requests.post(request_url, data=json.dumps(body), headers=headers)
    print("查询用户信息接口返回结果:" + response.text)
    if response.status_code == 200:
        result = json.loads(response.text)
        if result.get("code") == "00000":
            phone = result.get("data").get("phone")
            balance = result.get("data").get("balance")
            order_no = result.get("data").get("chargingOrderId")
            device_no = result.get("data").get("chargingDeviceNo")
            print("用户{}信息查询成功\n当前余额：{}\n充电订单号{}\n充电设备编号{}".format(phone, balance, order_no, device_no))
            user_dic = {"phone": phone, "balance": balance, "orderNo": order_no, "deviceNo": device_no}
            return user_dic
        else:
            print("查询用户信息失败，返回结果{}".format(response.text))
    else:
        print("查询用户信息接口调用失败")


"""
启动充电
参数 token 用户登录凭证 device_no 8位设备编码
"""


def start_charge(phone, token, device_no):
    request_url = Constant.CHARGE_DOMAIN_TEST + Constant.START_CHARGE_URL
    headers = {"FrontType": "egc-mobile-ui", "Content-Type": "application/json",
               "traceId": str(uuid.uuid4()).replace("-", ""), "Authorization": token}
    body = {"deviceNo": device_no, "chargeType": Constant.DEFAULT_CHARGE_TYPE,
            "feeRuleId": Constant.DEFAULT_CHARGE_FEE_RULE_ID}
    response = requests.post(request_url, data=json.dumps(body), headers=headers)
    print("查询用户信息接口返回结果:" + response.text)
    if response.status_code == 200:
        result = json.loads(response.text)
        if result.get("code") == "00000":
            order_no = result.get("data").get("chargingOrderId")
            print("用户{}启动充电成功，订单号{}".format(phone, order_no))
            return "success"
        else:
            print("用户{}启动充电失败".format(phone))
            return "fail"
    else:
        print("启动充电接口调用失败")
        return "fail"


"""
查询订单信息
参数 token 用户登录凭证 order_no订单编号
"""


def query_charging_order_info(token):
    user_dic = query_user_info(token)
    phone = user_dic.get("phone")
    order_no = user_dic.get("orderNo")
    if str(order_no) != "":
        request_url = Constant.CHARGE_DOMAIN_TEST + Constant.QUERY_ORDER_INFO_URL
        headers = {"FrontType": "egc-mobile-ui", "Content-Type": "application/json",
                   "traceId": str(uuid.uuid4()).replace("-", ""), "Authorization": token}
        body = {"chargingOrderId": order_no}
        response = requests.post(request_url, data=json.dumps(body), headers=headers)
        if response.status_code == 200:
            result = json.loads(response.text)
            if result.get("code") == "00000":
                order_info = result.get("data")
                print("查询订单信息".format(order_info))
            else:
                print("查询订单信息")
    else:
        print("当前用户{}没有充电中的订单".format(phone))


"""
结束充电
参数 token 用户登录凭证
"""


def stop_charge(token):
    user_dic = query_user_info(token)
    phone = user_dic.get("phone")
    order_no = user_dic.get("orderNo")
    device_no = user_dic.get("deviceNo")
    request_url = Constant.CHARGE_DOMAIN_TEST + Constant.STOP_CHARGE_URL
    headers = {"FrontType": "egc-mobile-ui", "Content-Type": "application/json",
               "traceId": str(uuid.uuid4()).replace("-", ""), "Authorization": token}
    body = {"deviceNo": device_no, "chargingOrderId": order_no}
    response = requests.post(request_url, data=json.dumps(body), headers=headers)
    if response.status_code == 200:
        result = json.loads(response.text)
        if result.get("code") == "00000":
            print("结束充电成功，返回结果{}".format(response.text))
            return "success"
        else:
            print("结束充电失败，返回结果{}".format(response.text))
            return "fail"
    else:
        print("结束充电接口调用失败")
        return "fail"


'''
模拟用户登录统一用户中心，默认密码111111
'''


def user_center_login(phone, pwd):
    pwd_md5 = md5(pwd.encode('utf-8')).hexdigest()
    print("phone={},pwd={}".format(phone, pwd_md5))
    
    param = {"country": "+086", "phone": "17688556401", "app_uuid": "10002", "os_type": "Android", "pwd": "fd7dd69c323d0f4026f46ea6199af76c"}
    body = str(json.dumps(param)).replace(" ", "")
    print("param=" + body)
    
    timestamp = "1571964750537"
    tmp_sign = "appid={}&timestamp={}&req_id={}&body={}&appkey={}" \
        .format(Constant.USER_CENTER_APP_ID_UAT, timestamp, timestamp, body, Constant.USER_CENTER_APP_KEY_UAT)
    # sign = str.upper(md5(tmp_sign.encode('utf-8')).hexdigest())
    sign = "C72DFB1F026F385C1B412CF0DF70EADB"
    request_url = Constant.USER_CENTER_DOMAIN_UAT + Constant.USER_CENTER_LOGIN_PWD + "?appid=100002&timestamp=" + timestamp + "&req_id=" + timestamp + "&sig=" + sign

    print(request_url)

    response = requests.post(request_url, data=body)
    print(response.text)


def check_account(phone):
    param = {"phone": phone, "country": "+086"}
    body = json.dumps(param)             
    timestamp = "1571964750537"
    tmp_sign = "appid={}&timestamp={}&req_id={}&body={}&appkey={}" \
            .format(Constant.USER_CENTER_APP_ID_UAT, timestamp, timestamp, body, Constant.USER_CENTER_APP_KEY_UAT)
    sign = str.upper(md5(tmp_sign.encode('utf-8')).hexdigest())
    print(sign)
    request_url = Constant.USER_CENTER_DOMAIN_UAT + Constant.USER_CENTER_CHECK_ACCOUNT + "?appid=100002&timestamp=" +\
                  timestamp + "&req_id=" + timestamp + "&sig=" + sign
    
    print(request_url)

    response = requests.post(request_url, data=param)
    print(response.text)


if __name__ == '__main__':
    print("start main...")
    
    # check_account(17688556401)

    # user_center_login("17688556401", "xia4698083")

    # 111111 = 96e79218965eb72c92a549dd5a330112
    # xia4698083 = fd7dd69c323d0f4026f46ea6199af76c
    # q123456 = c51cd8e64b0aeb778364765013df9ebe
    # print(md5("q123456".encode('utf-8')).hexdigest())

    access_token = user_login("17777000010", "111111")

    query_user_info(access_token)

    # query_charging_order_info(access_token, "20200629115480723500")

    # start_charge(access_token, "11548072")

    # stop_charge(access_token)
