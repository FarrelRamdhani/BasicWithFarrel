def Count(word, letter):
    pass

#Define Variable
flag_letter = 0

while True:
    word = input("Masukkan kalimat :")
    while flag_letter == 0:
        letter = input("Masukkan huruf yang ingin dicari :")
        if count(letter)!= 1:
            flag_letter = 0
            print("Masukkan ulang huruf")
    count = Count(word, letter)
    print("")
