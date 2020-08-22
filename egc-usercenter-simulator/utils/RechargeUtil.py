"""
模拟充值工具
"""

from hashlib import md5

# 签名加密key，固定值
sign_key = "AFDFDFJUIGIEOE789R85HFNJDS6HN"


"""
模拟用户充值（适用于所有环境），方法执行完毕之后，将返回的签名与充值金额更新到云端数据库用户信息表中
参数 union_id:用户union_id, money:充值金额
"""


def recharge(union_id, money):
    # 签名前字符串
    tmp_sign = union_id + str(int(round(money * 100))) + sign_key
    print('加密之前:', tmp_sign)

    # 计算签名（MD5加密）
    sign = md5(tmp_sign.encode('utf-8')).hexdigest()

    print('用户UNION_ID：', union_id)
    print('用户余额：', money)
    print('用户签名：', str.upper(sign))

    return str.upper(sign)


if __name__ == '__main__':
    recharge("04E860611778FAAB236C950C2376FCCE", 0.02)

