import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

dataFrame = pd.read_excel("merc.xlsx")

# Handle missing values if any
dataFrame = dataFrame.dropna()

print(dataFrame.head())
print(dataFrame.describe())
print()
print(dataFrame.isnull().sum()) 
sbn.histplot(dataFrame["price"])
plt.show()
sbn.countplot(x="year", data=dataFrame)
plt.show()
from sklearn.preprocessing import LabelEncoder

# Sayısal sütunları seçme
numeric_columns = dataFrame.select_dtypes(include=[np.number])

# Korelasyonu hesaplama (sadece sayısal sütunlar arasında)
print(numeric_columns.corr()["price"].sort_values())

sbn.scatterplot(x="mileage", y="price", data=dataFrame)
plt.show()

print(dataFrame.sort_values("price", ascending=True).head(20)) # ascending false olunca en yüksek fiyatı en yukarıda getirir.

print(len(dataFrame))
print(len(dataFrame)*0.01) #verinin %1'lik bir kısmını almak veya incelemek.
yuzde99df=dataFrame.sort_values("price",ascending=False).iloc[131:] #veri çerçevesinin ilk 131 satırını hariç tutarak, geriye kalan satırları döndürür.
print(yuzde99df)

# Önce yalnızca sayısal sütunları içeren bir DataFrame oluştur
numeric_df = dataFrame.select_dtypes(include=[np.number])
print(numeric_df.groupby("year").mean()["price"]) #yıllara göre gruplayıp fiyat ortalamasını al
print()
yuzde99numericdf=yuzde99df.select_dtypes(include=[np.number])
print(yuzde99numericdf.groupby("year").mean()["price"])

dataFrame=dataFrame.drop("transmission",axis=1) #transmission sütununu at.satır olsaydı axis=0.

dataFrame=dataFrame.select_dtypes(include=[np.number])
print(dataFrame[dataFrame["year"] != 1970].groupby("year").mean()["price"]) #1970 yılının değerlerini alma

y=dataFrame["price"].values
x=dataFrame.drop("price",axis=1).values #price hariç her şeyi al.
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.3, random_state=10)
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
x_train=scaler.fit_transform(x_train) #eğitirken fit.transform kullanılır, parametreleri öğrenir ve veriyi dönüştürür.
x_test=scaler.transform(x_test) #Öğrenilen parametrelerle veriyi dönüştürür.Hem eğitim hem test verisi için kullanılır.

from tensorflow import keras 
from keras.layers import Dense
from keras.models import Sequential

model=Sequential()
model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))

model.add(Dense(1))
model.compile(optimizer="adam", loss="mse")
#x_train, y_train: Eğitim verisi.
#validation_data=(x_test, y_test): Doğrulama (test) verisi.
#epochs=300: Model 300 kez eğitilecek.
#Verileri küçük gruplara (batch) ayırarak eğitimi daha verimli hale getirir.Genellikle 2'nin katları (32, 64, 128, 256) seçilir çünkü GPU optimizasyonları buna uygundur.
#Eğitim verisi: x_train içinde 10.000 örnek var. batch_size=100, epochs=10 diyebiliriz
model.fit(x=x_train,y=y_train,validation_data=(x_test,y_test),batch_size=200,epochs=300) #Model, her epoch sonunda x_test üzerinde tahmin yapar ve y_test ile karşılaştırarak doğrulama (validation) hatasını hesaplar.
kayipveri=pd.DataFrame(model.history.history)
kayipveri.plot()
plt.show()
from sklearn.metrics import mean_absolute_error
tahmindizisi=model.predict(x_test) #Modelin tahmin ettiği değerlerin dizisi.
print(tahmindizisi)
print()
print(mean_absolute_error(y_test, tahmindizisi))
plt.scatter(y_test,tahmindizisi) #y_test (gerçek değerler) ile tahmindizisi (tahminler) arasında bir saçılım grafiği (scatter plot) çizer.
plt.plot(y_test,y_test,"g--") #Eğer tüm noktalar bu çizginin üzerindeyse, model mükemmel tahmin yapmış demektir.
plt.show()

