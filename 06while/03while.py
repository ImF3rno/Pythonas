#amzinas ivedimas
kvadratas=0
while True:
    sk=int(input('sk= '))
    kvadratas=sk*sk
    print(f'skaicius {sk} kvadratas lygus {kvadratas}')
    atsakymas=input(('Ar dar noreite ivesti skaiciu? (T/N)'))
    if atsakymas!="T" and atsakymas!='t':
        break
