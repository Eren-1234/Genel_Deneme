from random import randint

sayi1 = randint(1,100)
sayi2 = randint(1,100)
sayi_list = []

sayi_list.append(sayi1)
sayi_list.append(sayi2)
sayi_list.sort() 
print(f"1.sayı: {sayi_list[0]} \n2.sayı: {sayi_list[1]}")
sayi_k = int(sayi_list[0])
sayi_b = int(sayi_list[1])
# Bu aşamaya kadar rastgele üretilen iki sayı sıralanmış bir şekilde listede bulunmaktadır
# Küçük sayımız sayi_k büyük sayımız sayi_b dir.

if int(sayi_list[0]) == int(sayi_list[1]):
    print("Sayılar eşit olduğundan program sonlandırılıyor.")

if (sayi_k % 2) == 0:
    sayi_k = sayi_k + 1

if (sayi_b % 2) == 0:
    sayi_b = sayi_b - 1
    
if sayi_list[0] != sayi_list[1]:
    adet = 0
    for i in range(sayi_k,sayi_b+1):
        if i%2 == 0:
            continue
        if i%2 == 1:
            adet += 1
            print(i,end=" ")
    print(f"\nToplam sayı adeti: {adet}")

        



