# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

listSize = int(input('Введите размер списка: '))
numberSearch = int(input('Введите число которое нужно найти: '))
listOne = list()
for i in range(listSize):
    listOne.append(random.randint(1, 10))
low = 0
high = listSize - 1
print(*listOne)
listOne.sort()
print(*listOne)

while low <= high:
    mid = low + (high - low) // 2
    if listOne[mid] > numberSearch:
        high = mid - 1
    elif listOne[mid] < numberSearch:
        low = mid + 1
    else:
        print(listOne[mid])
        break
else:
    print(listOne[mid])
