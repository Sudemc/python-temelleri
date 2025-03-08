import numpy as np
import pandas as pd

#Multi indeks

ilkindeksler=["cucemen", "cucemen", "cucemen", "aksoy", "aksoy", "aksoy"]
icindeksler=["sdm", "kursat", "nazike" ,"gulce","kubra","canan"]
birlesmisindeks=list(zip(ilkindeksler, icindeksler))
print(birlesmisindeks)
birlesmisindeks=pd.MultiIndex.from_tuples(birlesmisindeks)
print(birlesmisindeks)
print(type(birlesmisindeks))

famlist=[[20,"A"], [44, "B"],[45,"C"], [24,"K"], [36,"L"],[50,"M"]]
famNumpyList=np.array(famlist)
famDataframe=pd.DataFrame(famNumpyList, index=birlesmisindeks, columns=["yaş", "harf"])
print(famDataframe)
print()
print(famDataframe.loc["cucemen"])
print()
print(famDataframe.loc["cucemen"].loc["nazike"]) 
print()
famDataframe.index.names=["surname","name"] #indekslere başlık atama
print(famDataframe)
print()

#eksik veriler
veriler={"ist": [30,29,np.nan], "ank": [20,np.nan,30], "mlt": [40,30,15]} #içinde none olan sütunlar float döner olmayanlar int
havadrmDataframe=pd.DataFrame(veriler)
print(havadrmDataframe)
print()
print(havadrmDataframe.dropna()) #bir satırda eksik veri varsa o satırı çıkartır
print()
print(havadrmDataframe.dropna(axis=1, thresh=1)) #bir kolonda eksik veri sayısı thresh sayısı kadarsa o kolonu atar.
print()

#Data framede gruplandırma
dictmaas={"Department":["Software","Sales","Sales","Finance","Finance"],"Employee Name":["Can","Cem","Berk","Su","Ali"],"Salary":[100,150,200,250,300]}
maasDataFrame=pd.DataFrame(dictmaas)
print(dictmaas)
print()
gruplanmısdict=maasDataFrame.groupby("Department")
print(gruplanmısdict.count())
print(gruplanmısdict["Salary"].mean())  # Sadece maaş ortalamalarını alır
print()
print(gruplanmısdict["Salary"].min()) #Her departmandaki min maaşı döndürür.
print()
print(gruplanmısdict.describe()) #Departmanlara göre detaylı sayısal istatistik verir.
print()

#Data frameleri birleştirme
sozluk1={"İsim":["Ahmet","Sudem","Cem"],"Spor":["Koşu","Yüzme","Basketbol"],"Kalori":["300","100","200"]}
frame1=pd.DataFrame(sozluk1,index=[1,2,3])
print(frame1)
print()
print(frame1["İsim"].unique()) #Liste halinde istenen kolonu verir.
print(frame1["İsim"].nunique()) #Kaç tane olduğunu verir.
print(frame1["İsim"].value_counts) #Her birinden kaçar tane olduğunu verir.
sozluk2={"İsim":["Cenk","Elif","Yusuf"],"Spor":["Koşu","Yüzme","Badminton"],"Kalori":["300","150","250"]}
sozluk3={"İsim":["Matt","Hakkı","Deniz"],"Spor":["Yüzme","Yüzme","Kayak"],"Kalori":["250","350","100"]}
frame2=pd.DataFrame(sozluk2,index=[4,5,6])
frame3=pd.DataFrame(sozluk3,index=[7,8,9])
print(frame2)
print()
print(frame3)
print(pd.concat([frame1,frame2,frame3])) #Concat ile birleşrime (axis değeri yoksa default 0dır)
print()

msozluk1={"İsim":["Kazım","Hatice","Aydın"],"Kalori":[300,150,250]}
msozluk2={"İsim":["Kazım","Hatice","Aydın"],"Spor":["Koşu","Yüzme","Badminton"]}
def kalorihsp(kalori):
    return kalori*25
msozluk11=pd.DataFrame(msozluk1)
print(msozluk11["Kalori"].apply(kalorihsp)) #İstenen değer üstünden hesaplama
print()
print(msozluk11.isnull()) #Null değer var mı
mergedataframe1=pd.DataFrame(msozluk1)
mergedataframe2=pd.DataFrame(msozluk2)
print(mergedataframe1)
print()
print(mergedataframe2)
print()
print(pd.merge(mergedataframe1,mergedataframe2,on="İsim")) #Merge ile ortak sütün üstünden birleştirme yaptı.
print()
print(msozluk11.pivot_table(values="Kalori", index=["İsim"])) #Pivot table ile gruplama. Aynı indekslilerin ortalamasını alır.
#İndex parantezini kapatttıktan sonra aggfunc=np.sum yaparsan aynı indekslileri toplar.

pd.read_excel()#istenen excel tablosunu okur.
#yapılandataframe.to_excel() yeni tabloyu excele yazar.
