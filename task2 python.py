#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('X = '))
y = int(input('Y = '))
z = int(input('Z = '))
xyz =[x, y, z]
if not (xyz[0] or xyz[1] or xyz[2]) == (not xyz[0] and not xyz[1] and not xyz[2]):
    print(True)
else:
    print(False)







