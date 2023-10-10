#Вычислить и вывести на экран сумму кубов натуральных чисел от 1 до n включительно.
#Верхний предел должен вводиться с клавиатуры и не должен превышать числа 100.

try:
    i = -1
    sum = 0
    while not(1<=i<=100):
        i = (int)(input("Введите число от 1 до 100:"))
    for n in range(i+1):
        sum += n**3
    print("Сумма кубов целых чисел от 1 до " + (str)(i) + ": " + (str)(sum))
except:
    print("Неверные тип данных!")

#Выведите на экран таблицу умножения чисел от одного до девяти.

print("  ",' 1', '    2', '    3', '    4', '    5', '    6', '    7', '    8', '    9')
ar = [[],[],[],[],[],[],[],[],[]]
for i in range(1,10):
    for j in range(1,10):
        if i*j>=10:
            ar[i-1].append((str)(i*j))
        else:
            ar[i-1].append(" "+(str)(i*j))
    print((str)(i) + (str)(ar[i-1]))

#Задание с пары №1

alphabet = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'
print("--------------------")
for i in range (0,6):
    print("|" + alphabet[i * 10] + alphabet[i * 10 + 1] + "| " + "|" + alphabet[i * 10 + 2] + alphabet[i * 10 + 3] + "| " + "|" + alphabet[i * 10 + 4] + alphabet[i * 10 + 5] + "| " + "|" + alphabet[i * 10 + 6] + alphabet[i * 10 + 7] + "| " + "|" + alphabet[i * 10 + 8] + alphabet[i * 10 + 9] + "| ")
    print("--------------------")
print("|" + alphabet[60] + alphabet[61] + "| " + "|" + alphabet[62] + alphabet[63] + "| " + "|" + alphabet[64] + alphabet[65] + "| ")
print("--------------------")

#Задание с пары №2:

width = (int)(input("Enter width:"))
height = (int)(input("Enter height:"))
print("@   " * width)
for n in range(height):
    print("@   " + "    " * (width - 2) + "@")
print("@   " * width)
input()

