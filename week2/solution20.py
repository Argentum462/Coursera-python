# В кафе мороженое продают по три шарика и по пять шариков.
# Можно ли купить ровно k шариков мороженого?
k = int(input())
if k % 3 == 0 or k % 5 == 0 or k > 7:
    print('YES')
else:
    print('NO')