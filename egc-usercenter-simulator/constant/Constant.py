"""
测试环境配置，充电测试环境使用统一用户中心的UAT环境
"""
CHARGE_DOMAIN_TEST = "http://39.108.106.54:80/egc-cloudapicomponent"

USER_CENTER_DOMAIN_UAT = "https://uic-uat.evergrande.cn"

USER_CENTER_APP_ID_UAT = "100002"

USER_CENTER_APP_KEY_UAT = "!CDappkey#"

"""
开发环境配置，充电开发环境使用统一用户中心的TEST环境
"""
CHARGE_DOMAIN_DEV = "http://47.106.129.80:80/egc-cloudapicomponent"

USER_CENTER_DOMAIN_TEST = "https://uic-sit.evergrande.cn:6443"

USER_CENTER_APP_ID_TEST = "100002"

USER_CENTER_APP_KEY_TEST = "rhappkey124!"

USER_CENTER_LOGIN_PWD = "/v1/user/login_pwd"

USER_CENTER_CHECK_ACCOUNT = "/v1/user/check_account_upgrade"

# 模拟用户登录接口
USER_LOGIN_URL = "/admin/login"

# 查询登录用户信息接口
QUERY_USER_INFO_URL = "/api/charging/getChargingAccountInfo"

# 启动充电接口
START_CHARGE_URL = "/api/charging/startCharging"

# 停止充电接口
STOP_CHARGE_URL = "/api/charging/stopCharging"

# 查询充电中订单信息
QUERY_ORDER_INFO_URL = "/api/charging/queryChargingInfo"

# 默认充电方式，立即充电
DEFAULT_CHARGE_TYPE = 4

# 充电计费规则ID(根据充电桩绑定的小区来确定具体的值)
DEFAULT_CHARGE_FEE_RULE_ID = 1787

# 配置批量操作数据  登录手机号，登录密码，充电桩的8位设备编号
config_data = [
               {"phone": "13700000101", "password": "q1234567", "device_no": "11548039"},
               {"phone": "13700000102", "password": "q1234567", "device_no": "11548040"},
               {"phone": "13700000103", "password": "q1234567", "device_no": "11548041"},
               {"phone": "13700000104", "password": "q1234567", "device_no": "11548042"},
               {"phone": "13700000105", "password": "q1234567", "device_no": "11548086"},
               {"phone": "13700000106", "password": "q1234567", "device_no": "11548087"},
               {"phone": "13700000107", "password": "q1234567", "device_no": "11536788"},
               {"phone": "13700000108", "password": "q1234567", "device_no": "11548047"},
               {"phone": "13700000109", "password": "q1234567", "device_no": "11548048"},
               {"phone": "13700000110", "password": "q1234567", "device_no": "11548049"},
               {"phone": "13700000111", "password": "q1234567", "device_no": "11548081"},
               {"phone": "13700000112", "password": "q1234567", "device_no": "11548043"},
               {"phone": "13700000113", "password": "q1234567", "device_no": "11548082"},
               {"phone": "13700000114", "password": "q1234567", "device_no": "11548084"},
               {"phone": "13700000115", "password": "q1234567", "device_no": "11548083"},
               {"phone": "13700000116", "password": "q1234567", "device_no": "11548025"},
               {"phone": "13700000117", "password": "q1234567", "device_no": "11548023"},
               {"phone": "13700000118", "password": "q1234567", "device_no": "11548024"},
               {"phone": "13700000119", "password": "q1234567", "device_no": "11548026"},
               {"phone": "13700000120", "password": "q1234567", "device_no": "11548050"},
               {"phone": "13700000121", "password": "q1234567", "device_no": "11548027"},
               {"phone": "13700000122", "password": "q1234567", "device_no": "11548028"},
               {"phone": "13700000123", "password": "q1234567", "device_no": "11548029"},
               {"phone": "13700000124", "password": "q1234567", "device_no": "11548030"},
               {"phone": "13700000125", "password": "q1234567", "device_no": "11548031"},
               {"phone": "13700000126", "password": "q1234567", "device_no": "11548032"},
               {"phone": "13700000127", "password": "q1234567", "device_no": "11548033"},
               {"phone": "13700000128", "password": "q1234567", "device_no": "11548034"},
               {"phone": "13700000129", "password": "q1234567", "device_no": "11548035"},
               {"phone": "13700000130", "password": "q1234567", "device_no": "11548036"},
               {"phone": "13700000131", "password": "q1234567", "device_no": "11548037"}]

config_data_temp = [{"phone": "17688556401", "password": "xia4698083", "device_no": "11548037"}]

"""
开发环境数据库配置
"""
DATABASE_ENV_DEV = {"db_name": "hdsc_db", "db_host": "47.106.129.80", "db_port": "5432", "db_username": "hdsc_user_cha", "db_password": "gsYWNfe4"}

DATABASE_ENV_TEST = {"db_name": "hdsc_db", "db_host": "192.168.224.153", "db_port": "5432", "db_username": "hdsc_user_cha", "db_password": "gsYWNfe4"}

DATABASE_ENV_CDT_DEV = {"db_name": "hdsc_db", "db_host": "120.79.96.251", "db_port": "5432", "db_username": "hdsc_user_cha", "db_password": "gsYWNfe4"}

DATABASE_NAME_DEV = "hdsc_db"
DATABASE_HOST_DEV = "47.106.129.80"
DATABASE_PORT_DEV = "5432"
DATABASE_USERNAME_DEV = "hdsc_user_cha"
DATABASE_PASSWORD_DEV = "gsYWNfe4"

# 默认充值金额
DEFAULT_BALANCE = 99999

# 根据手机号查询用户信息
QUERY_USER_INFO_BY_PHONE = "select * from cha.user_info_overview where phone = '{}'"

# 更新用户余额与sign的sql语句
UPDATE_USER_BALANCE_SQL = "update cha.cha_user_info set sign = '{}', balance = {} where union_id = '{}'"

# 查询所有用户
QUERY_TOTAL_USER = "select * from cha.user_info_overview"


