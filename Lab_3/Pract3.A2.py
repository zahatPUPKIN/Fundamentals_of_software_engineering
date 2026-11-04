print('Ввод:')
parol = input('Введите пароль: ')
errors = []
up = False
digit = False
znaki_est = False
bukvi = False
znaki = ['*','-','#']
invalid = False

for i in parol:
    if i.isupper() == True:
        up = True    
    elif i in znaki:
        znaki_est = True
    elif i.isalpha() == True:
        bukvi = True
    elif i.isdigit() == True:
        digit = True
    else: 
        invalid = True

if len(parol) != 8:
    errors.append('Длина пароля не равна 8')
if up ==False:
    errors.append('В пароле отсутствуют заглавные буквы;')
if bukvi == False:
    errors.append('В пароле отсутствуют строчные буквы;')
if digit == False:
    errors.append('В пароле отсутствуют цифры;')
if znaki_est == False:
    errors.append('В пароле отсутствуют специальные символы;')
if invalid == True:
    errors.append('В пароле используются непредусмотренные символы.')
print('Вывод')
if not errors:
    print('Надежный пароль')
else:
    for i in errors:
        print(i)