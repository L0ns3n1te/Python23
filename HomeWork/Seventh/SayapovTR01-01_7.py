#Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно последние строки в количестве lines.
def read_last(lines, file):
    f = open(file)
    s = f.readlines()
    if not (lines > len(s)):
        lines = len(s) - lines
    else:
        return "Wrong number"
    for i in range(lines, len(s)):
        print(s[i][:-1])
    return ""

try:
    print(read_last(int(input("Input number:")), "article.txt"))
except:
    print("Wrong number")


#Составьте программу - простейший редактор текстовых файлов.
def text_editor():
    name = input("Введите имя файла:") + ".txt"
    try:
        f = open(name,"x")
    except FileExistsError:
        x = input("Файл с таким именем уже существует: чтобы файл перезаписать введите C, чтобы дополнить введите A:")
        if x == "C":
            f = open(name,"w")
        elif x == "A":
            f = open(name,"a")
        else:
            print("Отмена редактирования")
            return ""
    print("Режим ввода активирован, для выключения режима ввода введите пустую строку или *,^,&:")
    y = '1'
    while(y!="" or y!="*" or y!="^" or y!="&"):
        y = input(">")
        if y=="" or y=="*" or y=="^" or y=="&":
            f.close()
            break
        f.write(y + '\n')
    print("Завершение работы, файл сохранён")
    return ""

print(text_editor())