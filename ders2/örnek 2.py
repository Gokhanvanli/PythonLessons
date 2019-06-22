try:
    sayi_bir=int(input("lütfen birinci sayıyı giriniz : "))
    sayi_iki=int(input("lütfen ikinci sayıyı giriniz :"))
    toplam=sayi_bir+sayi_iki
    fark=sayi_bir-sayi_iki
    bolum=sayi_bir/sayi_iki
    carpim=sayi_bir*sayi_iki
    print("Sayıların Toplam",toplam,
    "\nSayıların Farkı",fark,
    "\n sayıların bolumu",bolum,
    "\n sayıların carpimi",carpim)
except ValueError :
    print("ValueError hatası")
except  ZeroDivisionError:
    print("Zero Division hatası")
except:
    print("hata mesaji")