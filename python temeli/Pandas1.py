import numpy as np
import pandas as pd

# Seriler oluşturma
sozluk={"ali": 15, "zeze": 26, "sdm": 18}
print(pd.Series(sozluk))
numbers=[15,26,18]
names=["ali", "zeze", "sdm"]
print(pd.Series(numbers))
print()
print(pd.Series(numbers, names))
print()
print(pd.Series(data=numbers, index=names))
print()
print(pd.Series(["ali", "zeze", "sdm"], [2,3,4]))
print()

puanListe=pd.Series([10,5,1], ["ali","zeze","sdm"])
print(puanListe)
print()
puanListe2=pd.Series([100,50,10],["ali", "zeze", "sdm"])
print(puanListe2)
print()
sonliste=puanListe+puanListe2
print(sonliste)
print()

puanListe3=pd.Series([15,25,35],["ali","sdm", "mert"])
listebirlesim=puanListe+puanListe3
print(listebirlesim) #sadecec aynı indexli verileri toplar

#Dataframe
data=np.random.randn(4,3)
dataframe=pd.DataFrame(data)
print(dataframe)
duzenliframe=pd.DataFrame(data, index=["a", "b", "c","d"],columns=["k","l","m"])
print(duzenliframe)
print()
print(duzenliframe["k"]) #columns (sütun) değerini verir
print()
print(duzenliframe.loc["a"]) # istenen satırları verir
print()
print(duzenliframe.iloc[1]) #1 indexli satırın değerlerini yazdırır
print()
duzenliframe["n"]=duzenliframe["k"]+ duzenliframe["l"]
print(duzenliframe)
print()
print(duzenliframe.drop("m", axis=1)) #kolon silmek için axis=1 satır silmek için 0.
duzenliframe.drop("n", axis=1, inplace=True) #inplace i true ya çevirmek değişikliği kalıcı kıldı.
print(duzenliframe) 
print()
print(duzenliframe.loc["b", "k"])
print(duzenliframe["l"] < 0 )
print(duzenliframe[duzenliframe["k"] <0]) #filtreleme

# indeks düzenleme
print(duzenliframe.reset_index()) 
indexlist=["aa", "bb", "cc", "dd"] #yazılanları kolon olarak ekler
duzenliframe["yeni indeks"]=indexlist
print(duzenliframe)
duzenliframe.set_index("yeni indeks", inplace=True) #yeni indeksi baş kolona alıp kalıcı hale getirdi
print(duzenliframe)

