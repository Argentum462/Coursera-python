# Дано натуральное число. Требуется определить, является ли год с данным
# номером високосным. Если год является високосным,
# то выведите YES, иначе выведите NO.
num = int(input())
if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0:
    print('YES')
else:
    print('NO')