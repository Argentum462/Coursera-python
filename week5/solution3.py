# Дано натуральное число n. Напечатайте все n-значные
# нечетные натуральные числа в порядке убывания.
n = int(input())
a = 1
while n > 0:
    a *= 10
    n -= 1

for i in range(a - 1, a // 10 - 1, -2):
    print(i, end=' ')
