# Напишите программу, которая на вход принимает два числа A и B, и возводит число А
# в целую степень B с помощью рекурсии.
# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def stepen(a, b):
    if b == 1:
        return a
    if b % 2 == 0:
        return stepen(a*a, b/2)
    else:
        return a*stepen(a, b-1)
    
a = int(input('Введите А: '))
b = int(input('Введите B: '))

print(stepen(a,b))
    