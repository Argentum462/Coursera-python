# Напишите программу, которая считывает два целых числа A и B
# и выводит наибольшее значение из них. Числа — целые от 1 до 1000.
num1 = int(input())
num2 = int(input())
c1 = num1 // num2
c2 = num2 // num1
print(((c1 * num1) + (c2 * num2)) // (c1 + c2))
