import heapq
import itertools
from collections import Counter


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


# 产生ABCD的全排列
itertools.permutations('ABCD')
# for item in itertools.permutations('ABCD'):
#     print(item)
# 产生ABCDE的五选三组合
itertools.combinations('ABCDE', 3)
# for item in itertools.permutations('ABCDE', 3):
#     print(item)
# 产生ABCD和123的笛卡尔积
itertools.product('ABCD', '123')
# for item in itertools.product('ABCD', '123'):
#     print(item)
# 产生ABC的无限循环序列
itertools.cycle(('A', 'B', 'C'))
# for item in itertools.cycle(('A', 'B', 'C')):
#     print(item)


words = [
      'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
      'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
      'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
      'look', 'into', 'my', 'eyes', "you're", 'under'
  ]
counter = Counter(words)
print(counter.most_common(3))
