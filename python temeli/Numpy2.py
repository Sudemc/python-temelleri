import numpy as np

arr13=np.arange(0,10)
print(arr13)
print(arr13[5])
print(arr13[3:8])

arr13[3:8]=100
print(arr13)
 
arr14=np.arange(0,10)
print(arr14)
dizininbirkısmı=arr14[2:6] 
print(dizininbirkısmı)
dizininbirkısmı[:]=78
print(arr14)

arr15=arr14.copy()
print(arr15)
arr15Slicing=arr15[1:9]
arr15Slicing[:]=90
print(arr15)
print(arr14)

listem=[[1,2,3 ],[10,20,30],[11,22,33]]
matrixdizim=np.array(listem)
print(matrixdizim)
print(matrixdizim[0])
print(matrixdizim[1,2])
print(matrixdizim[1:,1:])

yeniliste=[[0,1,2,3,4],[50,60,70,80,90],[11,22,33,44,55],[74,75,76,71,72]]
yenimatrix=np.array(yeniliste)
print(yenimatrix)
yenimatrix[[1,2,0]]

dizi=np.random.randint(1,100,20)
comparedizisi=dizi>24
print(dizi)
print(comparedizisi)
print(dizi[comparedizisi]) #sadece true olanları yazar
print(dizi+dizi)
print(dizi*3)
print(np.sqrt(dizi))
print(np.max(dizi))