import numpy as np

#numpy array
list1 = [1,2,3,4]
print(type(list1))

arr1 = np.array(list1)
print(arr1)
print(type(arr1))

matrixlist = [[1,2,3],[4,5,6],[7,8,9]]  
print(matrixlist)
print(type(matrixlist))

matrix = np.array(matrixlist)
print(matrix)
print(type(matrix))

#arange= array range
list2=list(range(0,5))
print(list2)
print(type(list2))

arr2 = np.arange(0,5)
print(arr2)
print(type(arr2))

#zeros
arr3 = np.zeros(5)
print(arr3)
print(type(arr3))

arr4 = np.zeros((4,3))
print(arr4)

#ones
arr5 = np.ones(5)
print(arr5)

arr6 = np.ones((4,3))
print(arr6)

#linspace (x,y,z) x ile y arasında z tane sayı oluşturur ve aralarındaki fark eşit olur
arr6 = np.linspace(0,10,5)
print(arr6)

#eye (birim matris)
arr7 = np.eye(5)
print(arr7)

#random (0-1 arasında rastgele sayılar)
arr8 = np.random.rand(5)
print(arr8)

arr9 = np.random.rand(4,3)
print(arr9)
print(type(arr9))

#randint (rastgele bir sayı döner son rakamı almaz)
arr10 = np.random.randint(1,10)
print(arr10)

list3=np.arrange(25)
print(list3)
arr11=np.random.randint(0,50,10)
print(arr11)    #10 tane 0-50 arasında rastgele sayı döner

#numpy array
arr12 = np.arange(30)
print(arr12)

arr12 = arr12.reshape(6, 5) 
print(arr12)
print(arr12.max())
print(arr12.min())
print(arr12.argmax()) #en büyük sayının indexini verir
print(arr12.argmin()) #en küçük sayının indexini verir
print(arr12.shape) #matrisin boyutunu verir

arr12 = arr12.reshape(5,6)
print(arr12)
print(arr12.shape)