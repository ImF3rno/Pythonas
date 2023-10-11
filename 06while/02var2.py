#ivedamas skaicius sk. Patikrinti ar jis pirminis
skaicius=int(input('Skaicius= '))
kiek=True
for i in range(1,skaicius+1//2):
    if skaicius%i==0:
        kiek=False
        break
if kiek:
    print(f'Skaicius {skaicius} pirminis')
else:
    print(f'Skaicius {skaicius} sudetinis')