kavos_kaina=float(input("Iveskite kavos kaina: "))
sumoketa=0
netinkama_moneta=0
tinkama_moneta=1
while sumoketa<kavos_kaina:
    pinigai=float(input("Imeskite 0.1, 0.2, 0.5 euro centus arba 1, 2 eurus: "))
    if pinigai in [0.1,0.2,0.5,1,2]:
        sumoketa+=pinigai
        likusi_suma=kavos_kaina-sumoketa
        if likusi_suma>0:
            print(f'Liko dar sumoketi: {round(likusi_suma,2)}')
            tinkama_moneta+=1
        elif likusi_suma==0:
            print('Skanios kavos')
        else:
            graza=sumoketa-kavos_kaina
            print(f'Graza jusu: {round(graza,2)}')
    else:
        print('Netinkama moneta. Meskite kita')
        netinkama_moneta+=1
if sumoketa>kavos_kaina:
    print('Skanios kavos')
print(f'Bandyta apgauti: {netinkama_moneta} kartus')
print(f'Tinkamu monetu: {tinkama_moneta} vnt.')