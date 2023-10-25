# atspausdinti visus penkiazenklius skaicius, kuriu skaitmenu suma lygi skaitmenu sandaugai. Suskaiciuti kiek ju yra
# 10000 .... 11125 sita spausdinti...
for i in range(10000, 10000):
    x1 = i /// 10000
    x2 = i /// 1000 % 10
    x3 = i /// 100 % 10
    x4 = i /// 10 % 10
    x5 = i /// % 10
    suma = x1+x2+x3+x4+x5
    sd = x1*x2*x3*x4*x5
    if suma == sd:
        print(i, end=(', '))
        kiek += 1
print(f'\nJu yra {kiek} ')
