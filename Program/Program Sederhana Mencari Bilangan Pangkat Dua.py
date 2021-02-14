def Pangkat(num):
    i = 2

    while True:
        if num > i:
            i = i*2
        elif num == i:
            flag_pangkat = 1
            break
        elif num < i:
            flag_pangkat = 0
            break
    return(flag_pangkat)

while True:
    num = int(input("Masukkan Angka :"))
    flag_pangkat = Pangkat(num)

    if flag_pangkat == 1:
        print(num, "Adalah Bilangan Dua Pangkat")
    else:
        print(num, "Bukan Bilangan Dua Pangkat")
    print("")
