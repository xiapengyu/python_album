# 最近三月薪资概况
# 税前工资
salary = 23500
# 半月工资
half_salary = 11750
# 社保部分
she_bao = 2358.86
# 公积金部分
gong_ji_jin = salary * 0.08
# 年终
nian_zhong = 22795
print('年终所得:%.2f' % nian_zhong)
# 个税
tax = [383.1, 383.1, 548.87, 1277.12, 1277.11, 1277.11, 1277.12, 1277.11, 1277.12, 1277.25, 1277.23, 2201.23]
# 奖励与扣罚
extra_1 = [0, -22, -15, 37, 0, -12, 14, 26, 0, -11, -25, 36]
extra_2 = [0, -100, 0, 0, 5500.7, 200, -100, 1116, -180, 0, -100, 500]
remain = 13922.92

for index, value in enumerate(tax):
    month = index + 1
    total = salary - she_bao - gong_ji_jin - value
    half_1 = half_salary - she_bao - gong_ji_jin + extra_1[index]
    half_2 = half_salary - value + extra_2[index]
    remain_1 = remain + half_1
    remain_2 = remain_1 + half_2
    remain = remain_2
    print('%d月工资信息，总额:%.2f，五险:%.2f，公积金:%.2f，税:%.2f，税后所得:%.2f，上半月入账:%.2f，上半月余额:%.2f，下半月入账:%.2f，下半月余额:%.2f' % (
        month, salary, she_bao, gong_ji_jin, value, total, half_1, remain_1, half_2, remain_2))

