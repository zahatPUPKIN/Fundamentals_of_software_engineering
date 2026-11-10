def draw_rectangle(n,m,symb):
    print(f'Прямоугольник {n}x{m}')
    for i in range(n):
        for s in range(m):
            print(symb, end='')
        print()
def draw_triangle(n,symb):        
    k = 1
    print('Правый треугольник:')
    for i in range(n):
        for s in range(k):
            print(symb, end='')
        k+=1    
        print()
def draw_ramka(n,m,symb):       
    print(f'Рамка {n}x{m}:')
    for i in range(n):
        for s in range(m):
            if i == 0 or i == n - 1 or s == 0 or s == m - 1:
                print(symb, end='')
            else:
                print(' '*length, end='')
        print()

n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
symb = (input('Символ для отрисовки: '))
length = len(symb)
draw_rectangle(n,m,symb)
draw_triangle(n,symb)
draw_ramka(n,m,symb)