m=[5,8,9,7,9,4,-1]
print(m)

user=["Jonas",18,1.78,True,[8,9,10,5,7]]
print(user[0])
print(user[4])
print(user[4][1])

suma=0
for i in m:
    suma+=i
print(suma)
kiekis=len(m)
print(kiekis)

for i in range(len(m)):
    print(f'm[{i}]={m[i]}')