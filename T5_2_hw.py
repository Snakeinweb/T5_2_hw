

word = input('Введите слово на латинице: ')
x = 0
y = 0
for ch in word:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o':
        x += 1
    else:
        y += 1
print ('Количество гласных:', x)
print ('Количество согласных:', y)  

if 'a' not in word or 'e' not in word or 'i' not in word or 'o' not in word: 
    print ('False')
else:
    print ('Количество \'a\' в слове', word+':', word.count('a'))
    print ('Количество \'e\' в слове', word+':', word.count('e'))
    print ('Количество \'i\' в слове', word+':', word.count('i'))
    print ('Количество \'o\' в слове', word+':', word.count('o'))

