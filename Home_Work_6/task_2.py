from random import randint

list_1 = [randint(1,5) for _ in range(10)]
list_2 = []
print(list_1)

a = 2
b = 3

for i in list_1:
    if i >= a and i <= b:
        list_2.append(i)
    else: 
        continue

print()
print(list_2)