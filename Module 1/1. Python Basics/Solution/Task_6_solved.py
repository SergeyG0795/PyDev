'''
Задача 6 «Следующее и предыдущее»

Напишите программу, которая считывает целое число и выводит текст,
аналогичный приведенному в примере (пробелы важны!).

'''
n = int(input())
print('The next number for the number ', n, " is ", n + 1, ".", sep='')
print('The previous number for the number ', n, ' is ', n - 1, '.', sep='')
