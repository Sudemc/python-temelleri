import numpy as np
import matplotlib.pyplot as plt

yaslist=[10,20,30,40,50,60,70]
kilolist=[40,50,55,60,65,70,75]
numpyYaslist=np.array(yaslist)
numpyKilolist=np.array(kilolist)
plt.plot(numpyYaslist, numpyKilolist, "r")#r red b blue g green gibi renkleri atayabilirsin
plt.xlabel("Yaş")
plt.ylabel("Kilo")
plt.title("Kilonun yaşa göre artışı")
plt.show()

numpydizi=np.linspace(0,10,20)
numpydizi2=numpydizi*numpydizi
plt.plot(numpydizi, numpydizi2, "g*-")
plt.show()

#birden fazla grafik çizme
plt.subplot(1,2,1)#ilk kaç sıra olacağı sonra kaç grafik olacağı sonra hangisini çizeceğini gir.
plt.plot(numpydizi, numpydizi2, "r--")
plt.subplot(1,2,2) #1 satırda 2 sütünda 2. grafiği yaz.
plt.plot(numpydizi2, numpydizi, "g*--")
plt.tight_layout() #grafikler arası mesafeyi ayarlar
plt.show()

myfigure=plt.figure()
figureAxes=myfigure.add_axes([0.2, 0.2, 0.7, 0.7]) #sol, alt, genişlik ve uzunluk değerleri
figureAxes.plot(numpydizi,numpydizi2, "g")
figureAxes.set_xlabel("x ekseni")
figureAxes.set_ylabel("y ekseni")
figureAxes.set_title("başlık")
plt.show()

newfigure=plt.figure(dpi=100) #parantez içine değer yazmazsan otomatik ayarlar ama dpi ne kadar yüksek olursa çözünürlüğü yüksek ve büyük olur.
yenieksen=newfigure.add_axes([0.1,0.1,0.9,0.9])
yenieksen.plot(numpydizi,numpydizi2, label="numpy dizisi**2") #label kısmı üstte not olarak yazılır.
yenieksen.plot(numpydizi, numpydizi2**2)
yenieksen.legend(loc=1) #yazdığın label notun yeri.
plt.show()

newfigure.savefig("newfig.png", dpi=150)#resim olarak kaydederken de dpi özelliğini verebilirsin.

(myfigure, yenieksen)=plt.subplots()
yenieksen.plot(numpydizi,numpydizi2,color="#3A95A8", alpha=0.4) #color ile hex kodunu verdiğin bir renk seçebilirsin. alpha değeri düştükçe şeffaflık artar.
yenieksen.plot(numpydizi,numpydizi+7,"g", linewidth=2.0, linestyle=":") #kalınlık ve çizgi tarzı
plt.show()

plt.scatter(numpydizi, numpydizi2)#dağıtılmış veri olarak getirir
plt.show()
dizi=np.random.randint(0,50,12)
print(dizi)
plt.hist(dizi)#veriyi histogram grafiğiyle verir
plt.show()
plt.boxplot(dizi) #veri yoğunluğunun nerede olduğunu daha iyi ifade eder.
plt.show()

