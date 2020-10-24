a=int(input("Ввеите число: "))
b=0
for i in range(1,a+1):
    if a%i==0:
        b+=1
if b==2:
    print("Число простое")
else:
    print("Число непростое")