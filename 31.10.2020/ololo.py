import random
kol_vo = int(input("Введите кол-во игр: "))
i = 0
ManWins = 0
ComputerWins = 0
ManCutChoose = 0
ManPaperChoose = 0
ManStoneChoose = 0
while i < kol_vo:
    print("\nВведите что вы хотите поставить: \n 1.Ножницы \n 2.Бумага \n 3.Камень")
    ManChoose = int(input("Ваш выбор: "))
    ComputerChoose = random.randint(1, 3)
    if ComputerChoose == 1:
        print("Компьютер выбрал Ножницы")
    elif ComputerChoose == 2:
        print("Компьютер выбрал Бумагу")
    elif ComputerChoose == 3:
        print("Компьютер выбрал Камень")

    if ManChoose == 1:
        ManCutChoose += 1
    elif ManChoose == 2:
        ManPaperChoose += 1
    elif ManChoose == 3:
        ManStoneChoose += 1

    if (ManChoose == 1 and ComputerChoose == 2)\
             or (ManChoose == 2 and ComputerChoose == 3)\
                or (ManChoose == 3 and ComputerChoose == 1):
        print("Вы выйграли!", "\n"*2)
        i += 1
        ManWins += 1
    elif ManChoose == ComputerChoose:
        print("Ничья!", "\n"*2)
    elif ManChoose > 3 or ManChoose < 1:
        print("Вы что-то неправильно ввели,попробуйте еще раз")
    else:
        print("Увы, но вы проиграли.", "\n"*2)
        i += 1
        ComputerWins += 1
print("Количество побед у человека:", ManWins)
print("Количество побед у компьютера:", ComputerWins)
print("Вы выбрали Ножницы ", ManCutChoose, "раза")
print("Вы выбрали Бумагу ", ManPaperChoose, "раза")
print("Вы выбрали Камень ", ManStoneChoose, "раза")
