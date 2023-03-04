import random
m = int(input('Введите длинну первого списка'))
n = int(input('Введите длинну второго списка'))

lst_1 = [random.randint(0, 10) for _ in range(m)]
lst_2 = [random.randint(0, 10) for _ in range(n)]

ls_1 = set(lst_1)
ls_2 = set(lst_2)
ls_3 = ls_1.intersection(ls_2)
lst = list(ls_3)
lst.sort()
print(lst)
