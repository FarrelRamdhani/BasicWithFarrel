def Modus(list_angka):
    count = 0
    terbanyak = list_angka[0]

    for i in list_angka:
        flag = list_angka.count(i)
        if flag >= count:
            count = flag
            terbanyak = i
    return(terbanyak)

while True:
    a = input("Masukkan list angka : ")

    list_angka = a.split()
    print("Modusnya adalah :", Modus(list_angka))
    print("")
