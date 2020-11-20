import sys


s1 = 'hello ' * 3
print(s1, end='\n')

s2 = 'world'
s1 += s2
print(s1, end='\n')
print('ll' in s1)
print('ll' not in s1)

# 切片，左闭右开
str2 = 'abc123456'
# c
print(str2[2])
# c12
print(str2[2:5])
# c123456
print(str2[2:])
# c246
print(str2[2::2])
# ac246
print(str2[::2])
# 654321abc
print(str2[::-1])
# 45
print(str2[-3:-1])

str1 = 'hello, world!'
print(len(str1))
print(str.capitalize(str1))
print(str.title(str1))
print(str.upper(str1))
print(str.find(str1, 'or', 10, 12))
print(str1.find('or'))
print(str1.find('shit'))
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
print(str.startswith(str1, 'H'))
print(str.startswith(str1, 'h'))
print(str1.endswith('!'))
print(str1.center(50, '*'))
print(str1.rjust(50, ' '))

str2 = 'a123456789'
print(str2.isdigit())
print(str2.isalpha())
print(str2.isnumeric())
print(str2.isdecimal())
print(str2.isalnum())

str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())

a, b = 5, 10
print('%d * %d = %d' % (a, b, (a * b)))
print('{0} * {1} = {2}'.format(a, b, (a * b)))
# 3.6以后版本提供的语法糖
print(f'{a} * {b} = {a * b}')
print(f'{a} * {b} = {a * b}')

list1 = [1, 3, 5, 7, 100]
print(list1)
print(len(list1))
list2 = ['hello'] * 3
print(list2)
# 下标(索引)运算
print(list1[0])  # 1
print(list1[4])  # 100
# print(list1[5])  # IndexError: list index out of range
print(list1[-1])  # 100
print(list1[-3])  # 5
list1[2] = 300
print(list1)  # [1, 3, 300, 7, 100]
# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])
# 通过for循环遍历列表元素
for elem in list1:
    print(elem)
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)

# 向列表添加删除元素
ist1 = [1, 3, 5, 7, 100]
# 添加元素
list1.append(200)
list1.insert(1, 400)
# 合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]
print(list1)  # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
print(len(list1))  # 9
# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1)  # [1, 400, 5, 7, 100, 200, 1000, 2000]
# 从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1)  # [400, 5, 7, 100, 200, 1000]
# 清空列表元素
list1.clear()
print(list1)  # []


fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
# 列表切片
fruits2 = fruits[1:4]
print(fruits2) # apple strawberry waxberry
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3) # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
fruits4 = fruits[-3:-1]
print(fruits4) # ['pitaya', 'pear']
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5) # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']


list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)

f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
f = [x **2 for x in range(1, 100)]
print(sys.getsizeof(f))
print(f)

f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
print(f)
for val in f:
    print(val)
