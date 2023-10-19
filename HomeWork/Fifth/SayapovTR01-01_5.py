# Три точки заданы своими координатами X(x1, x2), Y(y1, y2) и Z(z1, z2).
# Найти и напечатать координаты точки, для которой угол между осью абсцисс и лучом, соединяющим начало координат с точкой, минимальный.
# Вычисления оформить в виде процедуры.
import math
from random import randint


def d1(dot1, dot2, dot3):
    if max(abs(dot1[0] / dot1[1]), abs(dot2[0] / dot2[1]), abs(dot3[0] / dot3[1])) == abs(dot1[0] / dot1[1]):
        return dot1
    elif max(abs(dot1[0] / dot1[1]), abs(dot2[0] / dot2[1]), abs(dot3[0] / dot3[1])) == abs(dot2[0] / dot2[1]):
        return dot2
    elif max(abs(dot1[0] / dot1[1]), abs(dot2[0] / dot2[1]), abs(dot3[0] / dot3[1])) == abs(dot3[0] / dot3[1]):
        return dot3


dot1 = []
dot2 = []
dot3 = []
for i in range(2):
    dot1.append(randint(-100, 100))
    dot2.append(randint(-100, 100))
    dot3.append(randint(-100, 100))
print(dot1, dot2, dot3)
print(d1(dot1, dot2, dot3))
print()


# Найти все простые натуральные числа, не превосходящие n, двоичная запись которых представляет собой палиндром, т. е. читается одинаково слева направо и справа налево.

def d2(n):
    for i in range(0, n):
        if bin(i)[2:] == (bin(i)[2:])[::-1]:
            print(i, "(10)", " = ", bin(i)[2:], "(2)")
    return ""


n = int(input("Введите число n: "))
print(d2(n))
print()


# Задание с пары

def d3(x, y, a, b, dot4, dot5, dot6):
    R = math.sqrt((x - a) ** 2 + (y - b) ** 2)
    print("R = ", round(R, 3))
    print("Center: (", a, ",", b, ")")
    print(dot4, dot5, dot6)
    if math.sqrt((dot4[0] - a) ** 2 + (dot4[1] - b) ** 2) < R:
        print(dot4)
    if math.sqrt((dot5[0] - a) ** 2 + (dot5[1] - b) ** 2) < R:
        print(dot5)
    if math.sqrt((dot6[0] - a) ** 2 + (dot6[1] - b) ** 2) < R:
        print(dot6)
    return ""

dot4 = []
dot5 = []
dot6 = []
x = randint(-100, 100)
y = randint(-100, 100)
a = randint(-100, 100)
b = randint(-100, 100)
for i in range(2):
    dot4.append(randint(-100, 100))
    dot5.append(randint(-100, 100))
    dot6.append(randint(-100, 100))

print(d3(x, y, a, b, dot4, dot5, dot6))
