# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
#  и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

listt=input(("Введите элементы массива через пробел: ")).split(" ")
list_float=[float(item) for item in listt]

def minmax(list):
    import math
    a, b = math.modf(list[0])
    max=a
    min=a
    for i in range(1,len(list)):
        a, b = math.modf(list[i])
        if a > max: 
            max = a
        if a < min:
            min = a
    v=str(max-min)
    print(v[:4])

minmax(list_float)
