def print_faktor(x):
    print("Faktor dari", x, "Adalah :")
    for i in range(1, x+1):
        if x % i == 0:
            print(i)

while True:
    num = int(input("Masukkan Bilangan :"))
    print_faktor(num)
    print("")
