#Написать программу, которая будет делить введенные пользователем два вещественных числа и выводить результат на экран, сообщая об ошибке в случае деления на ноль.
import math

def d1(n1,n2):
    try:
        return round(((float)(n1))/((float)(n2)),7)
    except ValueError:
        return("Введины неверные данные!")
    except ZeroDivisionError:
        return("Нельзя делить на ноль!")
print(d1((input("Делимое: ")),(input("Делитель: "))))

#Рассчитать стоимость покупки с учетом скидки в 35%, которая предоставляется покупателю, если сумма покупки превышает 20 у.е..
#Сумму покупки ввести с клавиатуры, а результаты округлить до сотых (копейки, центы и т.д.). 
#Вывести на экран итоговую стоимость и размер предоставленной скидки.

def d2(sum):
    if sum > 20:
        return round((sum - sum*0.35),2) 
    else:
        return(sum)

try:
    sum = (float)(input("Cуммa: "))
    print("Итого: " + str((d2(sum))))
    if sum > 20:
        print("Скидка: " + (str)((sum - d2(sum))))
except:
    print("Неверные данные!")

#Напишите скрипт, который по введенному пользователем числу от 1 до 12, будет выводить на экран сообщение в виде названия месяца и времени года.
#Если пользователь введет недопустимое число, программа должна выдавать сообщение об ошибке.

seasons = ["зима","весна","лето","осень","зима"]
months = ["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]
try:
    n = (int)(input("Месяц №"))
    if 0<n<13: 
        print(months[n-1]+ ", " + seasons[n//3])
    else:
        print("Ошибка: неверные данные!")    
except:
    print("Ошибка: неверные данные!")

#Задание с пары №1
#Калькулятор квадратных уравнений

a = (float)(input("a = "))
b = (float)(input("b = "))
c = (float)(input("c = "))
if (a == 0 and b == 0 and c == 0):
    print("Бесконечное кол-во корней")
else:
    D = b**2 - 4*a*c
    N = 0
    x1 = None
    x2 = None
    if D>=0:
        if D==0:
            N = 1
            x1 = (-b)/2*a
        else:
            N = 2
            x1 = ((-b)-math.sqrt(D))/(2*a)
            x2 = ((-b)+math.sqrt(D))/(2*a)
    print("Дискриминант = " + (str)(D))

    if N == 2:
        print((str)(N) + " корня")
        print("x1 = " + (str)(x1) + " ,x2 = " + (str)(x2))
    if N == 1:
        print((str)(N) + " корнень")
        print("x = " + (str)(x1))
    if N == 0 or (a == 0 and b == 0 and c != 0):
        print("нет корней")

#Задание с пары №2
#Счётчик Дамилей

i = (int)(input("Сколько Дамилей?:"))
if (str(i))[-1] == "1" and not(((i>10) and (str(i))[-2] == "1")):
        print(str(i)+" Дамиль")
if ((str(i))[-1] == "2" or (str(i))[-1] == "3" or (str(i))[-1] == "4") and not(((i>10)) and (str(i))[-2] == "1" ):
        print(str(i)+" Дамиля")    
if (str(i))[-1] == "0" or (str(i))[-1] == "5" or (str(i))[-1] == "6" or (str(i))[-1] == "7" or (str(i))[-1] == "8" or (str(i))[-1] == "9" or ((i>10) and (str(i))[-2] == "1"):
        print(str(i)+" Дамилей")