# Задача 1
# Напишите программу, которая на вход принимает два числа A и B,
#  и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# Решение:

# def recApowB(a, b):
#     if b == 0:
#         return 1
#     return a * recApowB(a, b - 1)

# a = int(input('Введите число: '))
# b = int(input('Введите степень: '))
# print(recApowB(a, b))

# Задача 2
# Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# 2 2
# 4

# Решение:

# def sum(a, b):
#     if b == 0:
#         return 
#     else:
#         if b > 0:
#             return sum(a + 1, b - 1)
#         else:
#             return sum(a - 1, b + 1)

# print(sum(int(input()), int(input())))