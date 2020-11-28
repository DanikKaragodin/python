s = input("Введите строку в которой надо удалить группу символов: ")
while s.find("/*") != -1:
    firstPlace = s.find("/*")
    lastPlace = s.find("*/")
    i=firstPlace
    while i < lastPlace+2:
        s = s[:firstPlace] + s[firstPlace+1:]
        i+=1
print("Вот готовый вариант: ",s)
        