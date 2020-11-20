# 字面量语法
score = {'狄仁杰': 78, '李元芳': 98, '武则天': 67}
print(score)

# 构造器语法
dic1 = dict(狄仁杰=1, two=2, three=3, 马超=4)
dic1.update(马超=1)
print(dic1)

items2 = dict(zip(['a', 'b', 'c', 'd', 'e'], '1234'))
print(items2)

items3 = {num: num ** 2 for num in range(1, 10)}
print(items3)
