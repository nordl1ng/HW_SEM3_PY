# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

listt=input(("Введите элементы массива через пробел: ")).split(" ")
list_int=[int(item) for item in listt]

def couple(list):
    list_couple = []
    a = int(((len(list)-1)/2))
    for i in range(0,a+1):
        list_couple.append(list[i]*list_int[len(list)-1-i])
    print(f"Произведение элементов: {list_couple}")


couple(list_int)
