n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
print(f'Прямоугольник {n}x{m}')
for i in range(n):
    for s in range(m):
        print('#', end='')
    print()
k = 1
print('Правый треугольник:')
for i in range(n):
    for s in range(k):
        print('#', end='')
    k+=1    
    print()
print(f'Рамка {n}x{m}:')
for i in range(n):
    for s in range(m):
        if i == 0 or i == n - 1 or s == 0 or s == m - 1:
            print('#', end='')
        else:
            print(' ', end='')
    print()
