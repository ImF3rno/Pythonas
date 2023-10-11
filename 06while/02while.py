#ivedamas skaicius 12. Atspausdinti jo daliklius
#12=1 2 3 4 6 12 ju yra 6
#13=1 3 ju yra 2

skaicius=int(input('Skaicius= '))
kiek=0
for i in range(1,skaicius+1):
    if skaicius%i==0:
        print(i,end=(', '))
        kiek+=1
print(f'ju yra {kiek}')