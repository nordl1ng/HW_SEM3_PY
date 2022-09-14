# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

listt=input(("Введите элементы массива через пробел:")).split(" ")
list_int=[int(item) for item in listt]
print(list_int)

def summ_not_ev(list):
    summ = int (0)
    for i in range(1,len(list_int),2):
            summ += list_int[i]
    print(f'Сумма элементов на нечетных позициях равна {summ}')

summ_not_ev(list_int)
