import random
import time

for x in range(101):
    print(x)

for x in range(1, 101):
    print(x)

s = 0
for x in range(101):
    s += x
print(s)

for x in range(1, 101):
    if x % 2 == 0:
        print(x)

a = 0
while a <= 10:
    r = random.randint(10000, 100000)
    a += 1
    print(r)

print(time.strftime('%Y-%m-%d %H:%M:%S'))

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()

x = int(input('请输入正整数:'))
is_prime = True
for i in range(2, x + 1):
    if x % i == 0:
        is_prime = False
        break
if is_prime and x != 1:
    print('%d是素数' % x)
else:
    print('%d不是素数' % x)

answer = random.randint(1, 10)
count = 0
while True:
    count += 1
    number = int(input('请输入：'))
    if number > answer:
        print('大了一点')
    elif number < answer:
        print('小了一点')
    else:
        print('恭喜你猜对了')
        break
print('供猜了%d次' % count)

