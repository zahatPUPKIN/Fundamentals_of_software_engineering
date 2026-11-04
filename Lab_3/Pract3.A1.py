print('Ввод:')
x1 = int(input('Введите x1: '))
y1 = int(input('Введите y1: '))
x2 = int(input('Введите x2: '))
y2 = int(input('Введите y2: '))
print('Вывод:')
if x1 > 0 and y1>0 and x2>0 and y2>0 :
    print('Да, точки лежат в 1 четверти')
elif x1 > 0 and y1<0 and x2>0 and y2<0 :
    print('Да, точки лежат в 2 четверти')
elif x1 < 0 and y1<0 and x2<0 and y2<0 :
    print('Да, точки лежат в 3 четверти')
elif x1 < 0 and y1>0 and x2<0 and y2>0 :
    print('Да, точки лежат в 4 четверти')
else:
    print('Точки не лежат в одной четверти или находятся на осях ')