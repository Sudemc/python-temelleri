print("Fonksiyonlar")
# Fonksiyonlar, def anahtar kelimesi ile tanımlanır.
def fonksiyon():
    print("Merhaba")
fonksiyon()

fonksiyonum=("Hello")
def merhaba(isim="Sudem"):
    print(f"Merhaba {isim}")

merhaba("kemal")
merhaba()

def toplama(a,b):
    print(a+b)
toplama(5,6)

def superToplama(a,b,c):
    print(a+b+c)
superToplama(5,6,7)

def superToplama2(a,b,c):
    return a+b+c
degisken2=superToplama2(5,6,6) #return ile fonksiyonun sonucunu bir değişkene atayabiliriz. return olmazsa fonksiyonun sonucu None olur.
print(degisken2)

def wwww(**kwargs): #kwargs ile fonksiyona istediğimiz kadar argüman gönderebiliriz.
    return(kwargs)
print(wwww(a=1,b=2,c=3))
print(type(wwww(a=1,b=2,c=3))) #Burada dict olarak geliyor.(Return yazmassan noneType gelir.Toplama falan yaptırırsan int gelir.)

#map fonksiyonu ile fonksiyonları listelerle kullanabiliriz. Ama bizim bunu listeye çevirmemiz gerekir.
#Map fonksiyonu bir fonksiyon ve bir iterable obje alır ve her bir elemanı fonksiyona gönderir.

def kareal(x):
    return x**2
liste=[1,2,3,4,5]
print(list(map(kareal,liste)))
print(list(map(lambda x:x**2,liste))) #lambda fonksiyonu ile de fonksiyonları kullanabiliriz.

def kontrol(str):
    return "a" in str
liste2=["sudem","kemal","ayşe"]
print(list(map(kontrol,liste2)))
print(list(map(lambda str:"a" in str,liste2)))

#filter fonksiyonu map fonksiyonuna benzer ama sadece True dönen değerleri döndürür.
print(list(filter(kontrol,liste2)))
print(list(filter(lambda str:"a" in str,liste2)))
print(type(filter(kontrol,liste2))) #Burada filter objesi döner. Listeye çevirirsen list döner.
print(type(list(filter(kontrol,liste2)))) #Burada list döner.