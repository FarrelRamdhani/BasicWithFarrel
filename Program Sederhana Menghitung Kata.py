def Count(text):
    total = len(text.split())
    return(total)

while True:
    text = input("Masukkan Kalimat :")
    total = Count(text)
    print("Total kata dalam kalimat adalah sebanyak :", total)
