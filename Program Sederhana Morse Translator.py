Sandi = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
Huruf = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
Final_1 = ""
Final_2 = ""

def MorseToWord(Sandi, Huruf, input):
    i = 0

    while True:
        try:
            if input == Sandi[i]:
                output = Huruf[i]
                return(output)
                break
            else:
                i += 1
        except:
            output = "Tidak ditemukan"
            return(output)
            break

def WordToMorse(Sandi, Huruf, input):
    i = 0

    while True:
        try:
            if input == Huruf[i]:
                output = Sandi[i]
                return(output)
                break
            else:
                i += 1
        except:
            output = "Tidak ditemukan"
            return(output)
            break

#Main Program#

while True:
    print("Morse Translator")
    print("")
    print("Pilih 1 untuk menerjemahkan sandi morse")
    print("Pilih 2 untuk menerjemahkan kalimat")
    #Pilih fitur
    type = input("Pilihan : ")

    #Menerjemahkan MorseToWord
    if type == "1":
        Input_1 = input("Masukkan sandi morse : ")

        x = Input_1.split(" ")
        for i in range(len(x)):
            Output_1 = MorseToWord(Sandi, Huruf, x[i])

            Final_1 = Final_1 + Output_1
        print("Hasil Terjemahan :", Final_1)

    #Menerjemahkan WordToMorse
    elif type == "2":
        Input_2 = input("Masukkan kalimat : ")

        y = list(Input_2)
        for i in range(len(y)):
            if y[i] == " ":
                Output_2 = "  "
            else:
                Output_2 = WordToMorse(Sandi, Huruf, y[i])

            Final_2 = Final_2 + " " + Output_2
        print("Hasil Terjemahan :", Final_2)

    ##########################################
    else:
        pass
    #Reset#
    Final_1 = ""
    Final_2 = ""

    print("")
    print("")
