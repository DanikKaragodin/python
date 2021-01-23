import sqlite3
import argparse

# Проверка для выхода из программы


def check():
    print("Еще хотите что-то сделать?\n1.Да\n2.Нет")
    if (input("--> ") == "1"):
        print("Перечень комманд:\n1.Добавить\n2.Удалить\n3.Что-то найти\n4.Увидеть полную базу\n000. Выйти из программы")
        return False
    else:
        return True

# Вывод всей базы


def fullBase(c):
    for row in c.execute('SELECT * FROM book '):
        print(row)


# Парсер
parser = argparse.ArgumentParser()

parser.add_argument('-log', '--logs', action="store_true",
                    help="Вывод разработчика")
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


print("Здравствуйте,что вы хотите сделать с базой данных?\n1.Добавить\n2.Удалить\n3.Что-то найти\n4.Увидеть полную базу\n000. Выйти из программы")
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
                print( "#Была введена строка данных:", i  )
        conn.commit()

        exitFromProgramm = check()
# Удаление
    elif (vibor == "2"):

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
    elif (vibor == "3"):
        print("Какую информацию вы можете дать? Если вы не знаете что написать в одном из пунктов, то просто жмите ENTER")
        name = input("Введите имя: ")
        adress = input("Введите адрес: ")
        number = input("Введите номер телефона: ")
        email = input("Введите адрес электронной почты: ")
        print("Вот варианты: ")
        for row in c.execute('SELECT * FROM book WHERE (name = ? AND name != "") OR (adress = ? AND adress != "") OR (number = ? AND number != "") OR (email = ? AND email != "")  ', (name, adress, number, email)):
            print(row)
        exitFromProgramm = check()
# Полная база
    elif (vibor == "4"):
        fullBase(c)
        exitFromProgramm = check()
# Выход + неправильный ввод
    elif (vibor == "000"):
        print("Завершение программы. Удачи!")
        exitFromProgramm = True
    else:
        print("Вы ввели неправильную команду")

conn.close()
