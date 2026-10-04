i = 1
while i <=5:
    print(i)
    i+=1



while True:
    x=int(input("Введие число"))
    if x !=0:
        print("Вы не угадали")
    else:
        if x == 0:
            print("Вы угадали")
            break

while True:
    x=(input("Введие пароль"))
    if x != "python123":
        print("Введите заново")
    elif x == "python123":
        print("Доступ разрешен")
        break