#Даны целые числа a, b, c, являющиеся сторонами некоторого треугольника. Проверить истинность высказывания: «Треугольник со сторонами a, b, c является равносторонним».

import random #генерация случайных чисел

def Treugol(A,B,C):
    return (A < B+C) and (B < A+C) and (C < A+B)

a,b,c = [random.randrange(1,6) for i in range(0,3)] #random.randrange - возвращает случайное целое из диапазона
while not Treugol(a,b,c):
    a,b,c = [random.randrange(1,6) for i in range(0,3)]

print("Длина a: ", a)
print("Длина b: ", b)
print("Длина c: ", c)

prim = (a == b and a == c)
print("Треугольник является равносторонним: ", prim)
