print("Kapsam")
#Local, enclosing, global, built-in. Yani ilk başta en alt veya en içeride olan değişkene bakıyor. Orada bulamazsa bir üstte veya dışarıda olan değişkene bakıyor. Orada bulamazsa bu zamana kadar yazılmış eşitlemelere bakıyor (başka fonksinyonlar hariç). En sonunda onu da bulamazsa böyle bir kod var mı diye bakıyor. Onu da bulamazsa hata veriyor.

benimAdım = "sdm"
#Global
def adlar():
    benimAdım = "ahmet"
   #Enclosing
    def altAdlar():
        benimAdım = "ali"
        #Local
        print(benimAdım)
    altAdlar()
    
print(benimAdım) #Global
adlar() #Local 
altAdlar(benimAdım) #Built-in

