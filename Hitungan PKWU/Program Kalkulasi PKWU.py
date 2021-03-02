import PKWU

print("Selamat Datang di Kalkulator PKWU, Solusi Perhitungan Kewirausahaan")

flag_1 = 0

#Biaya HPP
hpp = 0

hppVariabel = 0
hppGajiProduk = 0
hppOverheadProduk = 0
hppJumlahProduk = 0
fixedCost = 0

#Kalkulasi Keuntungan
flag_2 = 0
#1 = Untung berdasarkan persen
#2 = Untung berdasarkan nominal

untungHpp = 0

untungNominal = 0
untungPersen = 0

untung = 0
untungTotal = 0

#Kalkulasi Gaji

#Kalkulasi Biaya Overhead

#Kalkulasi Biaya Variabel

while True:
    print("")
    print("Masukkan menu yang akan dipilih")
    print("1. Kalkulasi Biaya HPP \n2. Kalkulasi Keuntungan \n3. Kalkulasi Gaji \n4. Biaya Overhead \n5. Kalkulasi Biaya Variabel")

    try:
        flag_1 = int(input("Masukkan menu : "))
    except:
        print("Masukkan pilihan dengan benar!")
        flag_1 = 0

    if flag_1 == 1:
        print("")
        try:
            hppVariabel = int(input("Masukkan harga variabel per produk : "))
            hppGajiProduk = int(input("Masukkan gaji karyawan per hari : "))
            hppJumlahProduk = int(input("Masukkan jumlah produksi per hari :"))
            hppOverheadProduk = int(input("Masukkan biaya overhead : "))
        except:
            print("Masukkan pilihan dengan benar! \n")

        hpp, fixedCost = PKWU.hpp(hppVariabel, hppGajiProduk, hppJumlahProduk, hppOverheadProduk)

        print("Jadi, HPP produk ini : ", hpp)
        print("Jadi, Fixed Cost produk ini : ", fixedCost)

        hppVariabel = hppGajiProduk = hppJumlahProduk = hppOverheadProduk = 0

    elif flag_1 == 2:
        print("")
        print("Masukkan menu yang akan dipilih")
        print("1. Untung Persentase \n2. Untung Nominal")

        try:
            flag_2 = int(input("Masukkan menu : "))
        except:
            print("Masukkan pilihan dengan benar!")
            flag_2 = 0

        if flag_2 == 1:
            print("")
            try:
                untungHpp = int(input("Masukkan HPP : "))
                untungPersen = int(input("Masukkan Persentase Keuntungan : "))
            except:
                print("Masukkan pilihan dengan benar! \n")

            untung, untungTotal = PKWU.persentaseUntung(untungHpp, untungPersen)
            print("Jadi harga produk adalah :", untungTotal, "dan keuntungannya adalah :", untung)

            untungHpp = untungPersen = 0

        elif flag_2 == 2:
            print("")
            try:
                untungHpp = int(input("Masukkan HPP : "))
                untungNominal = int(input("Masukkan Nominal Keuntungan : "))
            except:
                print("Masukkan pilihan dengan benar! \n")

            untung, untungTotal = PKWU.nominalUntung(untungHpp, untungNominal)
            print("Jadi harga produk adalah :", untungTotal, "dan keuntungannya adalah :", untung, "%")

        else:
            pass

    elif flag_1 == 3:
        pass
    elif flag_1 == 4:
        pass
    elif flag_1 == 5:
        pass
    else:
        pass
    print("\n --------------------------------------------------------------------------------------")
