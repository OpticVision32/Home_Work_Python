# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

import random

listSize = int(input('Введите размер списка: '))
numberSearch = int(input('Введите число которое нужно найти: '))
listOne = []
countNumbers = 0

for i in range(listSize):
    listOne.append(random.randint(1, 10))
    if listOne[i] == numberSearch:
        countNumbers += 1
        
print(*listOne)
print()
print(countNumbers)

