def Morse(kode):
    #Define
    ii = 0
    j = 0
    Kalimat = []
    Kata = ""

    #Source
    Source = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    Huruf = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    x = kode.split(" ")
    for i in range(len(x)):
        while ii < len(Source):
            if x[i] == Source[ii]:
                Kalimat.append(ii)
                Kata = Kata + Huruf[ii]
                ii = 0
                break
            else:
                ii += 1

    return(Kata)

while True:
    kode = input("Masukkan kalimat dalam bahasa morse :")

    Kalimat = Morse(kode)
    print("Kalimat terjemahan adalah :", Kalimat)
    print("")
