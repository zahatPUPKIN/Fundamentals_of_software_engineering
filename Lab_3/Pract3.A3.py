import sys
print('Ввод:')
a = input('Введите предыдущее показание щетчика ')
b = input('Введите текущее показание щетчика ')
if int(a) > int(b):
    sys.exit('Предыдущее значение больше текущего')
UsesGaz = int(b) - int(a)
Oplata = 0
if UsesGaz <= 300:
    Oplata = 21
elif 300 < UsesGaz <= 600:
    Oplata = 21 + 0.06*(UsesGaz-300) 
elif 600 < UsesGaz <= 800:
    Oplata = 21 + 0.04*(UsesGaz-300)
elif UsesGaz > 800:
    Oplata = 21 + 0.025*(UsesGaz-300) 
Midle = round(Oplata / UsesGaz, 2)
print('Вывод:')
print('Предыдущее       Текущее       Использовано       К оплате       Ср. цена m^3')
print(" {:^9}".format(a), end=" ")
print(" {:^17}".format(b), end=" ")
print(" {:^11}".format(UsesGaz), end=" ")
print(" {:^20}".format(Oplata), end=" ")
print(" {:^11}".format(Midle))