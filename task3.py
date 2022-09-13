# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
#  и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

listt=input(("Введите элементы массива через пробел: ")).split(" ")
list_float=[float(item) for item in listt]

import math
max=0
min=1000
for i in range(0,len(list_float)):
    a, b = math.modf(list_float[i])
    if a > max: 
        max = a
    if a < min:
        min = a
h=float(max-min)
print(h)
