# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import random

x = random.randint(1, 10)
y = random.randint(1, 10)

print(f'Первое число - {x}')
print(f'Второе число - {y}')
print()

S = x + y
print(f'Сумма = {S}')
P = x * y
print(f'Произведение = {P}')

newX = S - y
newY = P // newX

print()
print(f'Первое число - {newX}')
print(f'Второе число {newY}')


