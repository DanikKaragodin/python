import random
seriya = 1
summa_v_seriyi = 0
kolvo_1 = 0
kolvo_2 = 0
dlina = 0
all_2 = 0
all_dlina = 0
not_zero = 0
max_not_zero = 0
while seriya != 21:
    print("Пошла", seriya, "серия:")
    while summa_v_seriyi != 12:
        random_cishlo = random.randint(0, 2)
        if(summa_v_seriyi + random_cishlo <= 12):
            print(random_cishlo, end="")
            summa_v_seriyi += random_cishlo
            dlina += 1
            all_dlina += 1
            if(random_cishlo == 1):
                kolvo_1 += 1
            elif(random_cishlo == 2):
                all_2 += 1
                kolvo_2 += 1
            if(random_cishlo != 0):
                not_zero += 1

    print(" ")
    print("Количество двоек в серии:", kolvo_2)
    print("Количество единиц в серии:", kolvo_1)
    print("Длина серии:", dlina)
    print("\n", "-"*10, "\n")
    if(not_zero > max_not_zero):
        max_not_zero = not_zero
    not_zero = 0
    kolvo_2 = 0
    kolvo_1 = 0
    dlina = 0
    summa_v_seriyi = 0
    seriya += 1
print("Среднее количество двоек:", all_2/20)
print("Средная длина:", all_dlina/20)
print("Максиальное количетсво НЕ нулей в одной серии:", max_not_zero)
