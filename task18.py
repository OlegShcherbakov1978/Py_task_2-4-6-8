# Задача 18: Требуется найти в массиве A[1..N] самый близкий
# по величине элемент к заданному числу X. Пользователь в первой
# строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

input_data = [-1, 1, 2, 3, 1, 6, 8, 4, 7]
res = 0
x = int(input('input number: '))
min = abs(input_data[0]-x)
for i in input_data:
    if abs(i - x) < min:
        min = abs(i - x)
        res = i
print(res)
