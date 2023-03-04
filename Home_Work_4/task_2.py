import random
n = 5
lst = [random.randint(1, 10) for _ in range(n)]
print(lst)
summ = 0
i = - 2
temp = 0
while i < len(lst):
    summ = lst[i] + lst[i - 1] + lst[i - 2]
    if summ > temp:
        temp = summ
    i += 1

print(temp)

