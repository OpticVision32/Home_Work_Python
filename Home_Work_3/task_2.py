# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

listSize = int(input('Введите размер списка: '))
numberSearch = int(input('Введите число которое нужно найти: '))
listOne = []
index = 0
closeInSize = 0
finishCloseInSize = numberSearch
for i in range(listSize):
    listOne.append(random.randint(1, 10))
print(*listOne)
for j in range(len(listOne) - 1):
    if numberSearch == listOne[j]:
        print(f'Число {numberSearch} есть в списке')
        break
    elif numberSearch > listOne[j]:
        closeInSize = numberSearch - listOne[j]
        if closeInSize < finishCloseInSize:
            finishCloseInSize = closeInSize
            index = j
    elif numberSearch < listOne[j]:
        closeInSize = listOne[j] - numberSearch
        if closeInSize < finishCloseInSize:
            finishCloseInSize = closeInSize
            index = j
else:
    print(f'Cамым близким по величине элемент к заданному числу {numberSearch} является число {listOne[index]}')
