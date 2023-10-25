kiek=0
for i in range(1000,10000):
    pirmi_du=i//100
    paskutiniai_du=i%100
    suma_dvieju=pirmi_du+paskutiniai_du
    kvadratas_dvieju=suma_dvieju**2
    if kvadratas_dvieju==i:
        print(i,end=(', '))
        kiek+=1
print(f'ju yra {kiek}')