def Count(word, letter):
    pass

#Define Variable
count = 0
letter_count = 0

while True:
    word = input("Masukkan kalimat :")
    while True:
        letter = input("Masukkan huruf yang ingin dicari :")
        for i in letter:
            letter_count = letter_count + 1
        if letter_count == 1:
            break
        else:
            print("Masukkan ulang huruf dengan benar!")
            letter_count = 0
    count = Count(word, letter)
    print("")
