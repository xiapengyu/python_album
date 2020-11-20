from math import sqrt

for n in range(100, 1000):
    low = n % 10
    mid = n // 10 % 10
    high = n // 100
    if (low ** 3 + mid ** 3 + high ** 3) == n:
        print('%d是水仙花数' % n)

prime = []
for num in range(2, 100):
    is_prime = True
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0 and num != i:
            is_prime = False
            break
    if is_prime and num != 1:
        prime.append(num)
print(prime)

j = 0
k = 1
for _ in range(20):
    j, k = k, j + k
    print(j, end=' ')


m = int(input('完美数校验，输入正整数:'))
s = 0
l = []
for i in range(1, m):
    if m % i == 0:
        l.append(i)
        s += i
if m == s:
    print('%d是完美数%s' % (m, l))

n = int(input('反转整数，输入正整数:'))
reversed_n = 0
while n > 0:
    reversed_n = reversed_n * 10 + n % 10
    n //= 10
print(reversed_n)


