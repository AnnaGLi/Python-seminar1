#задача 1
# 1.	Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

today = input('enter a number of the day from 1 to 7:')
if today == '6' or today == '7':
    print('-> yes, it is a weekend')
else:
    print('-> no, it is a working day')




