def Count(word, letter):
    count = 0
    for i in word:
        if i == letter:
            count+=1
    return count

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
    print("{0}, memiliki huruf {1}, sebanyak {2}".format(word, letter, count))
    print("")
