print("Metotlar")
#range() metodu belirli bir aralıktaki sayıları yazdırmak için kullanılır. Bellekte yer kaplamaz.
#range() metodu 3 parametre alabilir: başlangıç, bitiş ve artış miktarı
#range() metodu bir liste döndürmez.

benimlist = list(range(0,15)) #15 dahil değil
print(benimlist)
print()
print(list(range(4,76,17)))
print()
index = 0
for numara in list(range(8,80,9)):
    print(f"yeni sayı indexi: {index}, yeni sayı: {numara}")
    index = index + 1
print()

#enumerate() methodu bizim verdiğimiz listeye karşılık bir tuple verir bu tuple de birinci sayı index 2. sayı da listedeki değerdir.
#enumerate() methodu 2 parametre alır: liste ve başlangıç değeri
#enumerate() methodu bir liste döndürür.
for (index, numara) in enumerate(list(range(8,80,9)), 1):
    print(f"yeni sayı indexi: {index}, yeni sayı: {numara}")
print()

#randint() girilen değerler arasından rastgele sayı getirir.
from random import randint
print(randint(0,100))
print()

#shuffle() metodu verilen listeyi karıştırır.
from random import shuffle
mylist = list(range(0,10))
print(mylist)
shuffle(mylist)
print(mylist)
print()

#zip() metodu verilen listeleri birleştirir.
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = [10,20,30,40,50]
print(list(zip(list1,list2,list3)))
print(type(list(zip(list1,list2,list3))))
print(type(zip(list1,list2,list3)))
ziplenmis = list(zip(list1,list2,list3))
print(ziplenmis)

for num in ziplenmis:
    print(type(num)) #zip() metodu tuple döndürür
print()

ad="sudem"
yeniliste = [eleman for eleman in ad] #sudem stringini listeye çevirir
print(yeniliste)
print(type(yeniliste))
print()

ikincilist = [num * 5 for num in list(range(0,11))]
print(ikincilist)