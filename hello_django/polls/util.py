import base64
import datetime
import hashlib
import random

import jwt
from jwt import *
from rest_framework.exceptions import *

from hello_django import settings

ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_random_code(length):
    """获取随机验证码"""
    return ''.join(random.choices(ALL_CHARS, k=length))


def get_token():
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'userid': 10001
    }
    token = jwt.encode(payload, settings.SECRET_KEY).decode()
    print(token)
    return token


def check_token(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY)
    except InvalidTokenError:
        raise AuthenticationFailed('无效的令牌或令牌已经过期')


def gen_md5_digest(content):
    return hashlib.md5(content.encode()).hexdigest()


def get_base64(content):
    return base64.b64encode(content)


def main():
    # print(get_random_code(4))
    get_token()


if __name__ == '__main__':
    main()
