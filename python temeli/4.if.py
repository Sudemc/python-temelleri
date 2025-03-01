print("if-elif-else yapısı")
# if yapısı bir koşulun doğru olup olmadığını kontrol eder.Doğruysa if bloğu çalışır.
# if koşulu yanlışsa else bloğu çalışır.
# elif yapısı birden fazla koşulun kontrol edilmesini sağlar.

if 3 > 1:
    print("kod çalıştı")

x = 5
y = 4
a = 5
b= 6
if x > y:
    print("x, y'den büyük")
elif x < y:
    print("x, y'den küçük")
else:
    print("x, y'ye eşit")

if a > b and a > x:
    print("a, en büyük sayıdır")
elif a < b and a > x:
    print("a, ortanca sayıdır")
elif a < b and a < x:
    print("a, en küçük sayıdır")
else:
    print("sayılarda eşitlik var")


str="sudem"
if "a" in str:
    print("a harfi var")
else:
    print("a harfi yok")


if str=="Sudem":
    print("aynılar")
else:
    print("farklılar")

sozluk={"a":1, "b":2, "c":3}
anahtarlar=sozluk.keys()
if "a" in anahtarlar:
    value=sozluk["a"]
    print(f"a anahtarı:{value}")
else:
    print("a anahtarı yok")    

    

