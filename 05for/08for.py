#atspausdinti visus penkiazenklius skaicius kuriu skaitmenu suma lygi skaitemnu sandaugai 
#ir suskaiciuoti kiek ju yra..
#10000 iki 99999

kiek=0
for i in range(10000,100000):
    x1=i//10000
    x2=i//1000%10
    x3=i//100%10
    x4=i//10%10
    x5=i%10
    sandauga=x1*x2*x3*x4*x5
    suma=x1+x2+x3+x4+x5
    if suma==sandauga:
        print(i,end=(', '))
        kiek+=1
print(f'ju yra {kiek}')