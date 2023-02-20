# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input('Введите трёхзначное число: '))
summ = 0  


while (number > 0):
    summ += int(number % 10)
    number /= 10
    
print(summ)



