first_el = int(input("Введите первый элемент: "))
step = int(input("Введите разность: "))
size = int(input("Введите размер массива: "))
list_1 = []
for i in range(size - 1):
    if i == 0:
        list_1.append(first_el)
    first_el += step
    list_1.append(first_el)
    
print(list_1)