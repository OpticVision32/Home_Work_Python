# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

import random

list_size = int(input('Введите размер списка: '))
number_search = int(input('Введите число которое нужно найти: '))
list_one = []
count_numbers = 0

for i in range(list_size):
    list_one.append(random.randint(1, 10))
    
for j in list_one:
    if j == number_search:
        count_numbers += 1
        
print(*list_one)
print()
print(count_numbers)

