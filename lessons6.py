# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def sum_index(num):
#     w = 0
#     for i in range(len(num)):
#         if i % 2 != 0:
#             w += num[i]
#     print(f"Сумма равна: {w}")

# num = list(map(int, input("Введите числа через пробел:\n").split()))
# sum_index(num)


# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# num = list(map(float, input("Введите числа через пробел:\n").split()))
# new_num = [round(i % 1,2) for i in num if i % 1 != 0]
# print(max(new_num) - min(new_num))


# Задача. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# my_text = 'Напишите абв наабв програбвмму программу, удаляющую из этого абв текста все вабвс слова, содерабващие содержащие "абв"'

# def del_words(my_txt):
#     my_txt = list(filter(lambda y: 'абв' not in y, my_txt.split()))
#     return " ".join(my_txt)

# my_txt = del_words(my_text)
# print(my_txt)

# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов
# исходной последовательности.

# import random
# num = [random.randint(0, 10) for i in range(random.randint(5, 10))]
# result_list = list(filter(lambda y: num.count(y) == 1, num))
# print(f'Для последовательности\n {num}\n список уникальных элементов\n {result_list}')