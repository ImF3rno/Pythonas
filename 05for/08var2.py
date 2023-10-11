#atspausdinti visus penkiazenklius skaicius kuriu skaitmenu suma lygi skaitemnu sandaugai 
#ir suskaiciuoti kiek ju yra..
#10000 iki 99999

kiek=0
for i in range(10000,100000):
    suma=0
    sandauga=1
    sk=i
    for j in range(5):
        skaitmuo=sk%10
        sk=sk//10
        sandauga=sandauga*skaitmuo
        suma=suma+skaitmuo
    if suma==sandauga:
        print(i,end=(', '))
        kiek+=1
print(f'ju yra {kiek}')