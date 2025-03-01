print("Hataları Ele Alma")

def toplama(num1,num2):
    return num1 + num2
#yanlış bir değer (mesela yazı) girilirse hata verir. Bunu daha düzgün hale getirmek için;
while True:
    try:
        benimİnt = int(input("numaranızı giriniz ")) #ilk olarak burayı yapıyor hata olursa except e geçiyor hata olmazsa else ye geçiyor tamamen bittiğinde finally ye geçip bitiyor.
    except:
        print("gerçek sayılar giriniz ")
        continue
    else:
        print("teşekkürler ")
    finally:
        print("girdi yapıldı ")