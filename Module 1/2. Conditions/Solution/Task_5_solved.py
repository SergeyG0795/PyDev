'''
Задача 5 «Минимум из трех чисел»

Даны три целых числа. Выведите значение наименьшего из них.

'''

x = int(input())
y = int(input())
z = int(input())
m = x
if m > y:
    m = y
if m > z:
    m = z

print(m)
