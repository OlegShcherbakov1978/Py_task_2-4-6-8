# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно
# ввести с клавиатуры. Формула для получения n-го члена
# прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input('enter first el: '))
d = int(input('enter step: '))
n = int(input('enter number of digits: '))

dig_list = list()
for i in range(1, n+1):
    dig_list.append(a1 + (i-1)*2)

print(dig_list)
