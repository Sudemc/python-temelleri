import pandas as pd
import numpy as np

dataFrame=pd.read_excel("maliciousornot.xlsx")
print(dataFrame)
print(dataFrame.info())
print(dataFrame.describe())
print(dataFrame.corr()["Type"].sort_values())

import matplotlib.pyplot as plt
import seaborn as sbn
sbn.countplot(x="Type",data=dataFrame)
plt.show()
dataFrame.corr()["Type"].drop('Type').sort_values().plot(kind="bar") #bar grafiği halinde korelasyonu verir.
plt.show()

y=dataFrame["Type"].values #'Type' sütunu hedef değişken olarak atanıyor.
x=dataFrame.drop("Type",axis=1).values # 'Type' sütunu çıkarılıyor, geri kalanlar bağımsız değişkenler.
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=15) ## test_size=0.3 -> Verinin %30'u test, %70'i eğitim seti olarak ayrılıyor.
from sklearn.preprocessing import MinMaxScaler # Min-Max Normalizasyonu (Ölçeklendirme)
scaler=MinMaxScaler()
scaler.fit(x_train)  # Önce eğitim verisine göre scaler'ı eğit
x_train=scaler.transform(x_train) # Eğitim verisi 0-1 aralığına ölçekleniyor
x_test=scaler.transform(x_test) # Test verisi de aynı dönüşüme tabi tutuluyor.

import tensorflow as tf
from tensorflow import keras 
from keras.layers import Dense, Activation, Dropout
from keras.models import Sequential
from keras.callbacks import EarlyStopping

print(x_train.shape)
model=Sequential()
model.add(Dense(units=30,activation="relu")) #modelin ilk yoğun (dense) katmanı ekleniyor. 30 nöron, her nöron için ReLU (Rectified Linear Unit) aktivasyon fonksiyonu kullanılacak.
model.add(Dense(units=15,activation="relu")) #2. yoğun katmanda 15 nöron bulunacak.
model.add(Dense(units=15,activation="relu"))
model.add(Dense(units=1,activation="sigmoid")) #Son katmandaki aktivasyon fonksiyonu Sigmoid olacak, bu da çıktıyı [0, 1] arasında sıkıştırır, dolayısıyla ikili sınıflandırma (binary classification) için uygundur.

model.compile(loss="binary_crossentropy",optimizer="adam") #Bu satırda model derleniyor.
model.fit(x=x_train,y=y_train,epochs=500,validation_data=(x_test,y_test),verbose=1)
modelkaybi=pd.DataFrame(model.history.history)
modelkaybi.plot()
plt.show()

#monitor="val_loss": Validation (doğrulama) verisi üzerindeki kayıp (val_loss) değeri izleniyo.
#mode="min": Bu, kayıp değerinin minimuma inmesini beklediğimiz anlamına gelir. Yani, val_loss değeri minimuma ulaşmadığı sürece eğitim devam eder.
#verbose=1: Eğitim sırasında süreç hakkında bilgi verilecektir.
earlystopping =EarlyStopping(monitor="val_loss",mode="min",verbose=1,patience=25, min_delta=0.0001) #Yani, 25 epoch boyunca val_loss değeri iyileşmezse, erken durdurma işlemi devreye girer.
model.fit(x=x_train,y=y_train,epochs=500,validation_data=(x_test,y_test),verbose=1,callbacks=[earlystopping])
modelkaybi2=pd.DataFrame(model.history.history)
modelkaybi2.plot()
plt.show()

model = Sequential()
model.add(Dense(units=64, activation="relu"))
model.add(Dropout(0.5))  # Dropout ekleyin
model.add(Dense(units=32, activation="relu"))
model.add(Dropout(0.5))  # Dropout ekleyin
model.add(Dense(units=1, activation="sigmoid"))
model.compile(loss="binary_crossentropy",optimizer="adam")
model.fit(x=x_train,y=y_train,epochs=500,validation_data=(x_test,y_test),verbose=1)
modelkaybi3=pd.DataFrame(model.history.history)
modelkaybi3.plot()
plt.show()

from sklearn.metrics import classification_report, confusion_matrix
tahminlerimiz = (model.predict(x_test) > 0.5).astype("int32")
print(classification_report(y_test,tahminlerimiz))
print(confusion_matrix(y_test,tahminlerimiz))