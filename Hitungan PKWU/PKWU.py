def hpp(hppVariabel, hppGajiProduk, hppJumlahProduk, hppOverheadProduk):
    try:
        fixedCost = (hppGajiProduk/hppJumlahProduk) + hppOverheadProduk
        hpp = hppVariabel + fixedCost
    except:
        fixedCost = hpp = 0
    return hpp, fixedCost

def persentaseUntung(untungHpp, untungPersen):
    try:
        untung = untungHpp * (untungPersen / 100)
        untungTotal = untungHpp + untung
    except:
        untung = untungTotal = 0
    return untung, untungTotal

def nominalUntung(untungHpp, untungNominal):
    try:
        untungTotal = untungHpp + untungNominal
        untung = (untungNominal/untungHpp)*100
    except:
        untung = untungTotal = 0
    return untung, untungTotal

def karyawanBulan(karyawan, jumlah, gaji):
    try:
        biaya = karyawan * jumlah * gaji
    except:
        biaya = 0
    return biaya

def karyawanHari(karyawan, jumlah, gaji):
    try:
        biaya = (karyawan * jumlah * gaji)/30
    except:
        biaya = 0
    return biaya

def karyawanTahun(karyawan, jumlah, gaji):
    try:
        biaya = karyawan * jumlah * gaji * 12
    except:
        biaya = 0
    return biaya
