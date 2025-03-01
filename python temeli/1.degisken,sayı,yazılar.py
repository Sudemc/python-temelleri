print("Değişkenler")
#değişkenler bir değere atandıktan sonra RAM'de tutulur ve değişkenlerin değerleri değiştirilebilir

x=4
y=3

print(x*y)
print(x)
x=5
snc=1
print(snc)
snc=2
print(snc)

print("")
print("int, float ve matematiksel işlemler")

#işlem sırası: parantez içi, üs alma, çarpma ve bölme, toplama ve çıkarma şeklindedir. işlem önceki önceliği vardır.
#virgülle (,) ayrılan değerler tuple olarak kabul edilir. ab=2,25 ifadsi a=2, b=25 olarak kabul edilir.
#abs() mutlak değeri alır
print(x/y)
print(type(x/y))
print(x//y)
print(type(x//y)) ##pythonda (/) işlemi normal bölme işlemi yapar ama (//) işlemin sonucunu tam yapar.
print(x**y) #x üzeri y
print(type(x**y))

ab=2,25
c=4
print(ab*c) #bu işlem hata verir çünkü tuple değerler matematiksel işlem yapamaz
print(type(ab))
print(type(c))
print(type(ab*c))

yas=input("Yaşınızı giriniz: ")
print(yas*2) #matematiksel işlem yapmaz çünkü input fonksiyonu ile alınan değer string olarak kabul edilir
print(type(yas))
print(type(yas*2))
print(int(yas)*2) #bu şekilde string değeri integer'a çevirerek matematiksel işlem yapabiliriz
print(type(int(yas)*2))

print("")
print("Stringler ve string işlemleri")

#len() karakter uzunluğunu yazdırır
#upper() tüm karakterleri büyük yaparken capitalize() sadece ilk karakteri büyük yapar
#split() boşluk olan yerlerden stringlri ayırır.
#replace("a","b") a olan yerlere b yazdırır.
#strip() baştaki ve sondaki boşlukları siler
#lstrip() sadece baştaki boşlukları siler
#rstrip() sadece sondaki boşlukları siler
#join() stringleri birleştirir
#count() stringteki karakter sayısını yazdırır
#find() stringteki karakterin kaçıncı sırada olduğunu yazdırır
#startswith() stringin belirtilen karakterle başlayıp başlamadığını kontrol eder
#endswith() stringin belirtilen karakterle bitip bitmediğini kontrol eder
#center() stringi belirtilen karakterle ortalar

int_yas=int(yas)
print("Yaşınız: ", int_yas) #bu şekilde string ve integer değerleri birleştirebiliriz
print("Yaşınız: "+ str(int_yas)) #tüm değerleri string olarak birleştirebiliriz
print(f"Yaşınız: {int_yas}") #bu şekilde değişkenleri string olarak birleştirebiliriz
print("Yaşınız: {}".format(yas))
print(type(f"Yaşınız: {int_yas}"))
print(len(yas))

isim="sudem cücemen"

print(isim.split())
print(isim.split("e")) #e harfine göre stringleri ayırır
print(isim.upper())
print(isim.capitalize())
print(isim.replace("e","a"))
print(isim.strip())
print(isim.lstrip())
print(isim.rstrip())
print(isim.join("123xx"))
print(isim.count("e"))
print(isim.find("e"))
print(isim.startswith("s"))
print(isim.endswith("n"))
print(isim.center(50, "*"))

print(isim[2]) #2. karakteri yazdırır
print(isim[-1]) #son karakteri yazdırır
print(isim[1:4]) #1. karakterden 4. karaktere kadar yazdırır
print(isim[:4]) #baştan 4. karaktere kadar yazdırır 
print(isim[2:]) #2. karakterden son karaktere kadar yazdırır
print(isim[:-1]) #son karakter hariç tüm karakterleri yazdırır
print(isim[::-1]) #tersten yazdırır
print(isim[::2]) #2 karakter atlayarak yazdırır
print(isim[1:4:2]) #1. karakterden 4. karaktere kadar 2 karakter atlayarak yazdırır

