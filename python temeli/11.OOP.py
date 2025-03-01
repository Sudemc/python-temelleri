print("Obje Odaklı Programlama")

#instance & attribute

class Kahraman():
    def __init__(self,isim,yaş,meslek):
        self.isim = isim
        self.yaş = yaş
        self.meslek = meslek
kahraman1 = Kahraman("Superman",30,"Gazeteci")
print(kahraman1.isim)
print(kahraman1.yaş)
print(kahraman1.meslek)

class Kopek():
    def __init__(self,yas = 3):
        self.yas = yas 
    def inanYasi(self):
        return self.yas * 7
kopek1 = Kopek()
print(kopek1.yas)
print(kopek1.inanYasi())
kopek2 = Kopek(5)
print(kopek2.yas)
print(kopek2.inanYasi())

#inheritance
class Hayvan():
    def __init__(self):
        print("Hayvan sınıfı init çağrıldı")
    def method1(self):
        print("Hayvan sınıfı method1 çağrıldı")
    def method2(self):
        print("Hayvan sınıfı method2 çağrıldı")

class Class2(Hayvan):
    def __init__(self):
        Hayvan.__init__(self)
        print("Class 2 init çağrıldı")
    
    def method_3(self):
        print("method 3")
    #override
    def method_1(self):
        print("method 1 override")

kalıtımım= Class2()
kalıtımım.method1()
kalıtımım.method2()
kalıtımım.method_3()

#polymorphism
class Elma():
    def bilgi(self):
        print("Elma 100 kaloridir")
class Muz():
    def bilgi(self):
        print("Muz 150 kaloridir")
elma=Elma()
muz=Muz()
elma.bilgi()
muz.bilgi()

def bilgi(yemek):
    yemek.bilgi()
bilgi(elma)

#encapsulation
class Muhendis():
    def __init__(self):
        self.__maas=100
    def maas(self):
        print(self.__maas)
    def maasArttir(self,miktar):
        self.__maas+=miktar
muhendis=Muhendis()
muhendis.maas()
muhendis.maasArttir(50)
muhendis.maas()






