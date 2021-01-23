import sqlite3
import argparse

# Проверка для выхода из программы


def check():
    print("Еще хотите что-то сделать?\n1.Да\n2.Нет")
    if (input("--> ") == "1"):
        print("Перечень комманд:\n1.Добавить\n2.Изменить существующий контакт\n3.Удалить\n4.Что-то найти\n5.Увидеть полную базу\n000. Выйти из программы")
        return False
    else:
        return True

# Вывод всей базы


def fullBase(c):
    for row in c.execute('SELECT * FROM book '):
        print(row)


def advancedFullBase(c):
    inputValue = input(
        "По какому виду сортировки вам надо показать базу?\n1.По ID(стандартная)\n2.По Имени\n3.По адресу\n4.По номеру\n5.По электронной почте\n--> ")
    if int(inputValue) == 1:
        for row in c.execute('SELECT * FROM book '):
            print(row)
    elif int(inputValue) == 2:
        for row in c.execute('SELECT * FROM book ORDER BY name'):
            print(row)
    elif int(inputValue) == 3:
        for row in c.execute('SELECT * FROM book ORDER BY adress'):
            print(row)
    elif int(inputValue) == 4:
        for row in c.execute('SELECT * FROM book ORDER BY number'):
            print(row)
    elif int(inputValue) == 5:
        for row in c.execute('SELECT * FROM book ORDER BY email'):
            print(row)
    else:
        print("Вы ввели неправльную цифру, из за этого вы ничего не увидели")


# Парсер
parser = argparse.ArgumentParser()

parser.add_argument('-log', '--logs', action="store_true",
                    help="Вывод данных для разработчика")
args = parser.parse_args()

# Подключение базы
conn = sqlite3.connect('book.sqlite')
c = conn.cursor()

# Попытка создания таблицы
try:
    c.execute('''CREATE TABLE book(
        id INTEGER PRIMARY KEY,
        name text,
        adress text,
        number text,
        email text)''')
    if args.logs:
        print("#Автоматическое создание таблицы призошло успешно")
except(sqlite3.OperationalError):
    if args.logs:
        print("#Автоматическое создание таблицы призошло безуспешно(файл уже создан)")

# Переменная помогающая для выхода из программы
exitFromProgramm = False
# Подсчет последнего id в таблице

kolvoID = 0
for i in c.execute('SELECT * FROM book '):
    kolvoID += 1
if args.logs:
    print("# {} найденное количество id".format(kolvoID))


print("Здравствуйте,что вы хотите сделать с базой данных?\n1.Добавить\n2.Изменить существующий контакт\n3.Удалить\n4.Что-то найти\n5.Увидеть полную базу\n000. Выйти из программы")
# Сам процесс программы
while exitFromProgramm == False:
    vibor = input("--> ")
# Добавление
    if(vibor == "1"):
        kolvoID += 1
        name = input("Введите имя: ")
        adress = input("Введите адрес: ")
        number = input("Введите номер телефона: ")
        email = input("Введите адрес электронной почты: ")
        table = [(kolvoID, name, adress, number, email)]
        c.executemany(
            ''' INSERT OR REPLACE INTO book VALUES (?,?,?,?,?)''', table)
        if args.logs:
            for i in c.execute('SELECT * FROM book WHERE id = ? ', (kolvoID,)):
                print("#Была введена строка данных:", i)
        conn.commit()

        exitFromProgramm = check()
# обновления контактной информации
    elif(vibor == "2"):
        if(input("Нужно ли вам посмотреть полную Базу? \n 1. Да \n 0. Нет\n-->") == "1"):
            fullBase(c)
        print("Выберете id контакта, которого вы хотите изменить")
        idChoose = input("--> ")
        name = input("Введите имя(нажимайте Enter если не хотите менять): ")
        adress = input(
            "Введите адрес(нажимайте Enter если не хотите менять): ")
        number = input(
            "Введите номер телефона(нажимайте Enter если не хотите менять): ")
        email = input(
            "Введите адрес электронной почты(нажимайте Enter если не хотите менять): ")
        c.execute('SELECT * FROM book WHERE id = ? ', (idChoose))
        bufferbase = c.fetchone()
        bufferbase = list(bufferbase)
        print(bufferbase)
        if name != "":
            bufferbase[1] = name
        if adress != "":
            bufferbase[2] = adress
        if number != "":
            bufferbase[3] = number
        if email != "":
            bufferbase[4] = email
        if args.logs:
            for i in c.execute('SELECT * FROM book WHERE id = ? ', (idChoose)):
                print("#Была изменена эта строка: ", i)
        print(bufferbase)
        bufferbase=[tuple(bufferbase)]
        c.executemany('''INSERT OR REPLACE INTO book VALUES (?,?,?,?,?)''',bufferbase)
        conn.commit()
        exitFromProgramm = check()
# Удаление
    elif (vibor == "3"):

        if(input("Нужно ли вам посмотреть полную Базу? \n 1. Да \n 0. Нет\n-->") == "1"):
            fullBase(c)
        print("Выберете id контакта, которого вы хотите удалить")
        idChoose = input("-->")
        if args.logs:
            for i in c.execute('SELECT * FROM book WHERE id = ? ', (idChoose)):
                print("#Была удалена эта строка: ", i)
        c.execute('DELETE FROM book WHERE id = ? ', (idChoose))
        c.execute('UPDATE book SET id = (id-1) WHERE id > ? ', (idChoose))
        conn.commit()
        kolvoID -= 1
        exitFromProgramm = check()
# Нахождение
    elif (vibor == "4"):
        print("Какую информацию вы можете дать? Если вы не знаете что написать в одном из пунктов, то просто жмите ENTER")
        name = input("Введите имя: ")
        adress = input("Введите адрес: ")
        number = input("Введите номер телефона: ")
        email = input("Введите адрес электронной почты: ")
        findBase = []
        for row in c.execute('SELECT * FROM book WHERE name = ? ', (name,)):
            findBase.append(row)
        for row in c.execute('SELECT * FROM book WHERE adress = ? ', (adress,)):
            findBase.append(row)
        for row in c.execute('SELECT * FROM book WHERE number = ? ', (number,)):
            findBase.append(row)
        for row in c.execute('SELECT * FROM book WHERE email = ? ', (email,)):
            findBase.append(row)
       # print("Начальный этап: ", findBase)
      #  print("Длина: ",len(findBase))
        if findBase != set(findBase):
            index = 0
            i = 0
            FirstLen = len(findBase)
            while i != FirstLen:
               # print("i: ",i)
                for n in range(len(findBase)):
                    #print("n: ",n)
                    if(findBase[index] == findBase[n] and index != n):
                        index += 1
                        break
                    elif(n == len(findBase)):
                        findBase.pop(index)
                #print("index: ",index)
                i += 1

        print("Вот варианты: ", *set(findBase), sep='\n')
        exitFromProgramm = check()
# Полная база
    elif (vibor == "5"):
        advancedFullBase(c)
        exitFromProgramm = check()
# Выход + неправильный ввод
    elif (vibor == "000"):
        print("Завершение программы. Удачи!")
        exitFromProgramm = True
    else:
        print("Вы ввели неправильную команду")

conn.close()
