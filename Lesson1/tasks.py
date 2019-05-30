
def task1():
    var1,var2,var3="разработка", "сокет", "декоратор"
    print("содержание: "+ var1+"   тип: "+str(type(var1)))
    print("содержание: "+ var2+"   тип: "+str(type(var2)))
    print("содержание: "+ var3+"   тип: "+str(type(var3)))

    var1,var2,var3="\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430",\
                   "\u0441\u043e\u043a\u0435\u0442",\
                   "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440"
    print()

    print("содержание: "+ var1+"   тип: "+str(type(var1)))
    print("содержание: "+ var2+"   тип: "+str(type(var2)))
    print("содержание: "+ var3+"   тип: "+str(type(var3)))

def task2():
    var1, var2, var3 = b"class", b"function", b"method"
    print("содержание: " + str(var1) + "   тип: " + str(type(var1))+"  длина: "+str(len(var1)))
    print("содержание: " + str(var2) + "   тип: " + str(type(var2))+"  длина: "+str(len(var2)))
    print("содержание: " + str(var3) + "   тип: " + str(type(var3))+"  длина: "+str(len(var3)))

"""
def task3(): #так почему-то не работает...  записать в байтовом типе невозможно слова, состоящие из кириллицы.
# в байтовом типе могут быть только символы из ASCII
    try:
        var1= b"attribute"
    except SyntaxError:
        print("Нельзя")
    try:
        var2= b"класс"
    except SyntaxError:
        print("Нельзя")
    try:
        var3= b"функция"
    except SyntaxError:
        print("Нельзя")
    try:
        var4= b"type"
    except SyntaxError:
        print("Нельзя")
    
"""

def task4():
    var1, var2, var3, var4 = "разработка", "администрирование", "protocol", "standard"

    var1=var1.encode('utf-8')
    print(var1)
    print(var1.decode('utf-8'))
    print()
    var2=var2.encode('utf-8')
    print(var2)
    print(var2.decode('utf-8'))
    print()
    var3=var3.encode('utf-8')
    print(var3)
    print(var3.decode('utf-8'))
    print()
    var4=var4.encode('utf-8')
    print(var4)
    print(var4.decode('utf-8'))
    print()

def task5():
    import subprocess
    args = ['ping', 'yandex.ru'] #то же самое с youtube.com
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))


def task6():
    file = open("new.txt", "w")
    file.write("сетевое программирование\nсокет\nдекоратор")
    file.close()
    print(file) #проверили кодировку
    with open("new.txt") as f:
        for el in f:
            print(el)

    ''' #попытка декодировать cp1251 с помощью utf-8
    with open('new.txt', encoding='utf-8') as ff:
        for el_str in ff:
            print(el_str)
    '''


task6()
