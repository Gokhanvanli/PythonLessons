try:
    sayi_bir=int(input("lütfen bölünecek sayıyı giriniz"))
    sayi_iki=int(input("lütfen bölecek sayıyı giriniz"))
except ValueError as exp:
    print("İşlem hatası:",exp)
else:
    try:
        print(sayi_bir/sayi_iki)
    except ZeroDivisionError:
        print("sayı 0 değerine bölünmez")




