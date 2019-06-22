try:
    sayi=input("sayısal veri giriniz")
    print("gelen sayi",int(sayi))
    sayi=sayi/0
    print("islem sonu")
except ValueError as ex:
    print("ValueError")
    print("sistem hata mesajı",ex)
except ZeroDivisionError as ex:
    print("ZeroDivisionError")
    print("sistem hata mesajı", ex)
except Exception as ex:
    print("except")
    print("sistem hata mesajı",ex)