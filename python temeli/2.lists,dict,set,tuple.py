print("Listeler")
#listeler [] ile tanımlanır

listem=[1,2,3,4,5,6,7,8,9,10]
print(listem)
print(listem[3])
print(listem[1:4:2]) #1. karakterden 4. karaktere kadar 2şer atlayarak yazdırır
print(listem[::-1]) #tersten yazdırır
print(listem[::2]) #2şer atlayarak yazdırır
listem[2]=33 #2. karakteri 33 yapar
print(listem)
print(len(listem)) #listenin uzunluğunu yazdırır
print(5 in listem) #5 elemanının listede olup olmadığını kontrol eder
print(11 not in listem) #11 elemanının listede olmadığını kontrol eder
print()

print("Liste Metotları")

print(listem.index(5)) #5 elemanının kaçıncı sırada olduğunu yazdırır
print(listem.append(11)) #listenin sonuna 11 ekler
print(listem.pop()) #listenin son elemanını siler
print(listem.pop(3)) #3. elemanı siler
print(listem.remove(33)) #33 elemanını siler
print(listem.sort()) #listeyi sıralar
print(listem.reverse()) #listeyi ters çevirir
print(listem.count(5)) #5 elemanının listede kaç tane olduğunu yazdırır
listem2=[12,13,14,15]
print(listem.extend(listem2)) #listem2 listesini listem listesine ekler
print(listem.insert(3, 33)) #3. sıraya 33 elemanını ekler
print(listem.__getitem__(3)) #3. elemanı yazdırır
print(listem.__setitem__(3, 33)) #3. elemanı 33 yapar

print()
print("Karmaşık Listeler")
#remove metodu ile sadece ilk bulduğu elemanı siler ve iç içe olan listelerde içerideki listeyi silmez.
karmasik_liste=[0,[1,2],3,"s","s","sdm",["abc","def","ghi"]]
print(karmasik_liste)
print(karmasik_liste[5])
print(type(karmasik_liste[5]))
print(karmasik_liste[5][0])
print(karmasik_liste[6][0][1])
print(len(karmasik_liste))
print(karmasik_liste.count("s")) #sdm içindeki s harfinı saymaz
print(karmasik_liste.index("s")) #ilk bulduğu s harfinin kaçıncı sırada olduğunu yazdırır
print(karmasik_liste.index("s", 3)) #3. sıradan itibaren s harfinin kaçıncı sırada olduğunu yazdırır
karmasik_liste.remove("s") #sadece ilk bulduğu s elemanını siler.
print(karmasik_liste)
print()

print("Sözlükler")
#sözlükler {} ile tanımlanır

sozluk={"a":1, "b":2, "c":3, "d": {"e":4}}

print(sozluk)
print(sozluk["a"])
sozluk["a"]=5
print(sozluk)
print(sozluk.keys()) #sözlükteki anahtarları yazdırır
print(sozluk.values()) #sözlükteki değerleri yazdırır
print(sozluk.items()) #sözlükteki anahtar ve değerleri yazdırır
print(sozluk.get("d")) #a anahtarının değerini yazdırır
sozluk["a"]=6
print(sozluk)
sozluk["d"]["e"]=7
print(sozluk)
print(sozluk.pop("a")) #a anahtarının değerini yazdırır ve siler
print(sozluk)
e_degeri = sozluk["d"]["e"]
print(e_degeri)
sozluk2={"e":5, "f":6}
print(sozluk.update(sozluk2)) #sozluk2 sözlüğünü sozluk sözlüğüne ekler update metodunun yan etkisi olarak none döner.
print(sozluk)
print()

print("Setler")
#setler {} ile tanımlanır
#setlerde listeden farklı olarak, aynı elemanlar bir kere yazılır ve sıralı değildir.

ranList=["a", 1,2,"b", 2,1]
ranSet=set(ranList)
print(ranList)
print(ranSet)
ranSet.add("c")
print(ranSet)
print()

print("Boş set tanımlama")
bossetim=set()
print(bossetim)
print(type(bossetim))
bossetim.add(1)
print(bossetim)
