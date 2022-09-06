#Задача 2
#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

x = int(input('enter the first coordinate x: '))
y = int(input('enter the first coordinate y: '))
while x and y != 0:
    if x and y > 0:
        print('this coordinates belong to the 2nd quarter')
    elif (x > 0) and (y < 0):
        print('this coordinates belong to the 4nd quarter')
    elif (x < 0) and (y < 0):
        print('this coordinates belong to the 3nd quarter')
    elif (x < 0) and (y > 0):
        print('this coordinates belong to the 1st quarter')
else:
    print('enter value different than zero')





