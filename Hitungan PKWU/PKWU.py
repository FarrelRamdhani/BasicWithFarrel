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

def karyawanBulan(karyawan, jumlah):
    try:
        biaya = karyawan * jumlah
    except:
        biaya = 0
    return biaya

def karyawanHari(karyawan, jumlah):
    try:
        biaya = (karyawan * jumlah)/30
    except:
        biaya = 0
    return biaya

def karyawanTahun(karyawan, jumlah):
    try:
        biaya = karyawan * jumlah * 12
    except:
        biaya = 0
    return biaya

def overheadHari(overheadGas, overheadListrik, overheadAir, overheadLain):
    try:
        overhead = (overheadGas + overheadListrik + overheadAir + overheadLain)/30
    except:
        overhead = 0
    return overhead

def overheadBulan(overheadGas, overheadListrik, overheadAir, overheadLain):
    try:
        overhead = (overheadGas + overheadListrik + overheadAir + overheadLain)
    except:
        overhead = 0
    return overhead

def overheadTahun(overheadGas, overheadListrik, overheadAir, overheadLain):
    try:
        overhead = (overheadGas + overheadListrik + overheadAir + overheadLain)*12
    except:
        overhead = 0
    return overhead
