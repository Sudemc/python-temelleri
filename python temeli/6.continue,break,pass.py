print("Contunie, Break ve Pass")
# break döngüyü tamamen durdurur.
# continue döngünün mevcut adımını atlar sonraki adımlardan devam eder.
#oraya hangi kodu koyacağımızı bilmiyorsak veya daha ne yazacağımıza karar veremediysek hata vermemesi için kullanılır.
listt=[5,3,6,7,23,695]
for x in listt:
    print(x*8+10)

for y in listt:
    if y==23:
        break
    print(y)

for z in listt:
    if z%2==0:
        continue
    print(z)

for t in listt:
    pass 

