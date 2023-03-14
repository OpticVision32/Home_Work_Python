num_rows = int(input('Введите количество строк: '))
num_columns = int(input('Введите количество столбцов: '))


def print_operation_table(f, num_rows, num_columns):
    x = int(input('Введите номер строки: '))
    y = int(input('Введите номер столбца: '))
    lst_1 = []
    for i in range(1, num_rows + 1):
        lst_2 = []
        for j in range(1, num_columns + 1):
            lst_2.append(i * j)
        lst_1.append(lst_2)

    for i in lst_1:
        print(*i)

    print(f'Ваше число: {f(x,y)}')


print_operation_table(lambda x, y: x * y, num_rows, num_columns)
