import pandas as pd
import seaborn as sbn
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from keras.layers import Dense
from keras.models import Sequential
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Veri setini yükleme
dataFrame = pd.read_excel("bisiklet_fiyatlari.xlsx")
print("Veri setindeki sütunlar:", dataFrame.columns)

# Bağımlı değişken (etiket - hedef değer) ve bağımsız değişkenleri (özellikler) belirleme
y = dataFrame["Fiyat"].values  # .values kullanarak NumPy dizisine çeviriyoruz
x = dataFrame[["BisikletOzellik1", "BisikletOzellik2"]].values  # Özellikleri seçiyoruz

# Veriyi eğitim ve test setlerine ayırma
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=15)
print("Eğitim verisi boyutu:", x_train.shape)
print("Test verisi boyutu:", x_test.shape)

# Özellikleri normalize etme (1 ile 2 arasına ölçeklendirme)
scaler = MinMaxScaler(feature_range=(1, 2))
scaler.fit(x_train)  # Eğitimi sadece eğitim verisiyle yapıyoruz
tx_train = scaler.transform(x_train)  # Eğitim verisini ölçeklendiriyoruz
x_test = scaler.transform(x_test)  # Test verisini ölçeklendiriyoruz

# Yapay sinir ağı modelini oluşturma
model = Sequential()
model.add(Dense(4, activation="relu"))  # İlk gizli katman (4 nöron, ReLU aktivasyon fonksiyonu)
model.add(Dense(4, activation="relu"))  # İkinci gizli katman
model.add(Dense(4, activation="relu"))  # Üçüncü gizli katman
model.add(Dense(1))  # Çıkış katmanı (tek bir değer üretecek)

# Modeli derleme (optimizer: RMSprop, loss: ortalama kare hata - mse)
model.compile(optimizer="rmsprop", loss="mse")

# Modeli eğitme (250 epoch boyunca eğitim yapılıyor)
history = model.fit(x_train, y_train, epochs=250)

# Kayıp değerlerinin (loss) görselleştirilmesi
loss = history.history["loss"]  # Her epoch'taki hata değerleri
sbn.lineplot(x=range(len(loss)), y=loss)
plt.xlabel("Epoch")
plt.ylabel("Kayıp (Loss)")
plt.title("Eğitim Kaybı (Loss) Grafiği")
plt.show()

# Modelin eğitim ve test verisindeki performansını değerlendirme
trainLoss = model.evaluate(x_train, y_train, verbose=0)
testLoss = model.evaluate(x_test, y_test, verbose=0)
print("Eğitim Verisi Kayıp Değeri:", trainLoss)
print("Test Verisi Kayıp Değeri:", testLoss)

# Modelin test verisindeki tahminlerini alma
testTahminleri = model.predict(x_test)

tahminDF = pd.DataFrame(y_test, columns=["Gerçek Y"])  # Gerçek değerleri DataFrame'e ekleme
testTahminleri = pd.Series(testTahminleri.reshape(-1))  # Tahminleri uygun şekle getirme
tahminDF = pd.concat([tahminDF, testTahminleri], axis=1)
tahminDF.columns = ["Gerçek Y", "Tahmin Y"]

print(tahminDF.head())  # İlk birkaç tahmini ekrana yazdırma

# Gerçek ve tahmin edilen değerlerin scatter plot ile görselleştirilmesi
sbn.scatterplot(x="Gerçek Y", y="Tahmin Y", data=tahminDF)
plt.xlabel("Gerçek Değerler")
plt.ylabel("Tahmin Edilen Değerler")
plt.title("Gerçek vs Tahmin Edilen Değerler")
plt.show()

# Model performans metrikleri (MAE ve MSE)
mae = mean_absolute_error(tahminDF["Gerçek Y"], tahminDF["Tahmin Y"])
mse = mean_squared_error(tahminDF["Gerçek Y"], tahminDF["Tahmin Y"])
print("Ortalama Mutlak Hata (MAE):", mae)
print("Ortalama Kare Hata (MSE):", mse)

# Veri setinin istatistiksel özetini gösterme
print(dataFrame.describe())

yeniBisikletOzellikleri=[[1750,1749]]
yeniBisikletOzellikleri=scaler.transform(yeniBisikletOzellikleri)
print(model.predict(yeniBisikletOzellikleri))

from keras.models import load_model
# Modeli kaydetme
model.save("bisiklet_fiyat_modeli.h5")

# Modeli yükleme
loaded_model = load_model("bisiklet_fiyat_modeli.h5")

# Yüklenen model ile tahmin yapma
yeniTahmin = loaded_model.predict(yeniBisikletOzellikleri)
print("Yüklenen model ile tahmin:", yeniTahmin)
