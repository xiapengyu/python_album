from utils import SmartchargeUtil
from utils import RechargeUtil

filePath = "D:\\logs2\\target_phone.txt"

with open(filePath, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line is not None and line.strip() != '':
            print(line.strip())
            access_token = SmartchargeUtil.user_login(line.strip(), '111111')
            SmartchargeUtil.query_user_info(access_token)


