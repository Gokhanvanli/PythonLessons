try:
    telefon_numarası=input("Lütfen telefon numaranızı giriniz : ")
    print("Telefon numaranız : ",int(telefon_numarası))
except ValueError:
    print("işlem hatası")
    print("Lütfen geçerli bir sayı giriniz")
except ZeroDivisionError:
    print("işlem hatası")
    print("sıfıra bölünme hatası")