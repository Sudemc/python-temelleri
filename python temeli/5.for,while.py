print("For döngüsü")
# for döngüsü bir veri yapısındaki elemanları tek tek döngü içinde işlememizi sağlar.
# for döngüsü range() fonksiyonu ile de kullanılabilir.
# for döngüsü içindeki elemanlar bir koşula bağlı olarak işlenir.

lister = [1,2,3,4,5,6]
for num in lister:
    if num % 2 == 0:
        print(num)
    else:
        print("tek sayı")

tuple2 = (1,3,5,7,9,0)
for a in tuple2:
    print(a+8)

degisikliste = [(12.4,34.7),(48.4,86.6),(45.2,78)]
for (x,y) in degisikliste:
    print(x)
    print(y)

sozlukk = {"a" : 8, "b" : 70, "c" : 20}        
sozlukk.items() #sözlükteki anahtar ve değerleri yazdırır
for anahtar, deger in sozlukk.items():
    print(anahtar)
    print(deger)
    
print()
print("While döngüsü") 
#While, önündeki değer True olduğu sürece çalışır.   

list2=[2,65,2,3,8,1]
while 3 in list2:
   print("üçü geçmedik")
   list2.pop()

num = 0
while num < 10:
    if num == 6:
        break
    print(num)
    num = num + 1
    
       