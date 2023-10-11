#petriuko pazymiai ir vidurkis
kiekis=int(input('Kiek turi pazymiu='))
suma=0
for i in range(1,kiekis+1):
    paz=int(input(f'Iveskite {i}-aji pazymi='))
    if 1<=paz<=10:
        suma+=paz
    else:
        print('Blogas pazimys ir kartokite ivedima')

vid=suma/kiekis
print(f'Petriuko vidurkis {vid}')