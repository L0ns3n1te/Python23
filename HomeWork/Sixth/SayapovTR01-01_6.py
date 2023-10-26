#Дан двумерный массив размером 3x3. Определить максимальное значение среди элементов третьего столбца массива;
#максимальное значение среди элементов второй строки массива. Вывести полученные значения.
from random import randint


def d1(k, arr):
    n = -1000000
    m = -1000000
    for i in range(k):
        n = max(n, arr[i][2])
        m = max(m, arr[1][i])
    print(n)
    print(m)
    return ""


arr = [[randint(-1000, 1000), randint(-1000, 1000), randint(-1000, 1000)],
       [randint(-1000, 1000), randint(-1000, 1000), randint(-1000, 1000)],
       [randint(-1000, 1000), randint(-1000, 1000), randint(-1000, 1000)]]
print(arr[0])
print(arr[1])
print(arr[2])
print(d1(3, arr))


#Дан двумерный массив размером mxn. Сформировать новый массив заменив положительные элементы единицами, а отрицательные нулями.
#Вывести оба массива.
def d2(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] > 0:
                arr[i][j] = 1
            elif arr[i][j] < 0:
                arr[i][j] = 0
    for i in range(len(arr)):
        print(arr[i])
    return ""


arr0 = []
arr01 = []
w = int(input("Введите высоту двумерного массива:"))
h = int(input("Введите ширину двумерного массива:"))
for i in range(w):
    arr0.append([])
    arr01.append([])
    for j in range(h):
        x = randint(-1000, 1000)
        arr0[i].append(x)
        arr01[i].append(x)

for i in range(len(arr0)):
    print(arr0[i])
print("<>")
print(d2(arr01))


#Дана целая квадратная матрица n-го порядка.
#Определить, является ли она магическим квадратом, т. е. такой матрицей, в которой суммы элементов во всех строках и столбцах одинаковы.
def d3(arr):
    n = sum(arr[0])
    for i in range(1, len(arr)):
        if not (n == sum(arr[i])):
            return False
    for i in range(len(arr)):
        m = 0
        for j in range(len(arr[i])):
            m += arr[j][i]
        if m != n:
            return "Не является магическим квадратом"
    return "Является магическим квадратом"


# Квадрат Марса (взят с wikipedia.com)
arr3 = [[12, 25, 8, 21, 4],
        [5, 13, 26, 9, 17],
        [18, 6, 14, 22, 10],
        [11, 19, 2, 15, 23],
        [24, 7, 20, 3, 16]]
print(d3(arr3))

arr4 = [[1, 2, 3],
        [3, 2, 1],
        [1, 2, 3]]

print(d3(arr4))
print()


#Определить, является ли заданная целая квадратная матрица n-го порядка симметричной (относительно главной диагонали).
def d4(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != arr[j][i]:
                return "Несимметрична"
    return "Симметрична"


arr5 = [[1, 2, 3],
        [2, 2, 1],
        [3, 1, 3]]
arr6 = [[1, 0, 3],
        [2, 2, 1],
        [3, 1, 3]]
print(d4(arr5))
print(d4(arr6))
print()


#Дана прямоугольная матрица. Найти строку с наибольшей и строку с наименьшей суммой элементов.
#Вывести на печать найденные строки и суммы их элементов.
def d5(arr):
    mn = int("9" * 100)
    mx = -int("9" * 100)
    n1 = 0
    n2 = 0
    for i in range(len(arr)):
        if mn > sum(arr[i]):
            mn = sum(arr[i])
            n1 = i
        if mx < sum(arr[i]):
            mx = sum(arr[i])
            n2 = i
    print("Наибольшей суммой элементов обладает строка №", n2 + 1, ":", arr[n2], "-->", mx)
    print("Наименьшей суммой элементов обладает строка №", n1 + 1, ":", arr[n1], "-->", mn)
    return ""


arr7 = [[randint(-1000, 1000), randint(-1000, 1000), randint(-1000, 1000)],
        [randint(-1000, 1000), randint(-1000, 1000), randint(-1000, 1000)],
        [randint(-1000, 1000), randint(-1000, 1000), randint(-1000, 1000)]]
print(arr7[0])
print(arr7[1])
print(arr7[2])
print(d5(arr7))


#Дана действительная матрица размером n х m, все элементы которой различны. В каждой строке выбирается элемент с наименьшим значением.
#Если число четное, то заменяется нулем, нечетное - единицей. Вывести на экран новую матрицу.

def d6(arr):
    for i in range(len(arr)):
        if arr[i][arr[i].index(min(arr[i]))] % 2 == 0:
            arr[i][arr[i].index(min(arr[i]))] = 0
        elif arr[i][arr[i].index(min(arr[i]))] % 2 != 0:
            arr[i][arr[i].index(min(arr[i]))] = 1
        print(arr[i])
    return ""


arr8 = []
w1 = int(input("Введите высоту двумерного массива:"))
h1 = int(input("Введите ширину двумерного массива:"))
for i in range(w):
    arr8.append([])
    for j in range(h):
        x = randint(-1000, 1000)
        arr8[i].append(x)
    print(arr8[i])
print("<>")
print(d6(arr8))
