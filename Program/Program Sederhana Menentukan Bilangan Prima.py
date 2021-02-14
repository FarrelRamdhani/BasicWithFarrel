def Prima(num):
    i = 0
    flag_prima = 0

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag_prima = 2
                break
            else:
                flag_prima = 1
    else:
        flag_prima = 0
    return(i, flag_prima)

while True:
    num = int(input("Masukkan Bilangan :"))
    i, flag_prima = Prima(num)

    if flag_prima == 1:
        print(num, "Adalah Bilangan Prima")
    elif flag_prima == 2:
        print(num, "Bukan Bilangan Prima")
        print(i, "Kali", num//i, "=", num)
    else:
        print(num, "Bukan Bilangan Prima")
    print("")
