# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

x = int(input('Введите первую сторону шоколадки: '))
y = int(input('Введите первую сторону шоколадки: '))
k = int(input('Введите количество долек, которое хотите отломить: '))

if (1 < k < x * y and k % x == 0 or k % y == 0):
    print('Yes')
else:
    print('No')
