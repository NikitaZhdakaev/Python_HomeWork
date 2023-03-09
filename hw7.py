# Задача 1: 

# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

# # Ввод:
# # пара-ра-рам рам-пам-папам па-ра-па-дам 
# # Вывод:
# # Парам пам-пам

# Решение:

# def poem_vowels_count(testing_poem: list, checking_alfabet: set()) -> tuple[int]:

#     list_of_vowels_number = []

#     for i in range(len(testing_poem)):
#         frase_vowels_number = int()
#         for j in range(len(checking_alfabet)):
#             frase = testing_poem[i]
#             count = sum(map(lambda frase: 1 if checking_alfabet[j] in frase else 0, frase))
#             frase_vowels_number += count
#         list_of_vowels_number.append(frase_vowels_number)

#     result = list_of_vowels_number
#     return result

# message_for_user_1 = 'Введите стихотворение: '
# message_for_user_2 = 'Парам пам-пам'
# message_for_user_3 = 'Пам парам'
# alfabet_vowels = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]

# poem = input(message_for_user_1).split(' ')
# result = poem_vowels_count(testing_poem = poem, checking_alfabet = alfabet_vowels)

# if sum(result) / len(result) == result[0]:
#     print(message_for_user_2)
# else:
#     print(message_for_user_3)

# Задача 2:

# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# Ввод:
# print_operation_table(lambda x, y: x * y)
# Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

# Решение:

# def print_operation_table(operation, num_rows, num_сolumns):
#     arr=[[operation(i,j) for i in range(1,num_rows+1)] for j in range(1, num_сolumns+1)]
#     for i in arr:
#         print(*[f"{x:>3}"for x in i])
# line = int(input("Введите количество строк: "))
# columns = int(input("Введите количество столбцов: "))
# print_operation_table(lambda x,y: x*y,line,columns)