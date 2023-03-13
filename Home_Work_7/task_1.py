vowels = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']
song = input('Введите стих: ').lower().split()
i = 0
count_vowels = list()
for item in song:
    for j in item:
        if j in vowels:
            i += 1
    count_vowels.append(i)
    i = 0

if len(set(count_vowels)) == 1:
    print('Парам пам-пам')
else :
     print('Пам парам')
