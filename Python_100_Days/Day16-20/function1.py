# 生成式，推导式的使用，可以用来生成列表（list）、集合（set）和字典（dict）
my_dic = {'HD': 105, 'WK': 254, "BGY": 58, 'JD': 98}
prices = {key: value for key, value in my_dic.items() if value > 100}
print(prices)


names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# scores = [[None] * 3 for _ in range(5)]
scores = [[None] * len(courses) for _ in range(len(names))]
for row, name in enumerate(names):
    print(row, name)
    for col, course in enumerate(courses):
        print("-", col, course)
        scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
        print(scores)

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
  {'name': 'IBM', 'shares': 100, 'price': 91.1},
  {'name': 'AAPL', 'shares': 50, 'price': 543.22},
  {'name': 'FB', 'shares': 200, 'price': 21.09},
  {'name': 'HPQ', 'shares': 35, 'price': 31.75},
  {'name': 'YHOO', 'shares': 45, 'price': 16.35},
  {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(3, list1))
print(heapq.nsmallest(3, list1))
print(heapq.nlargest(2, list2, key=lambda x: x['price']))
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))