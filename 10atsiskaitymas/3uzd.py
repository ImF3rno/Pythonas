import random

n=int(input("Pasirinkite teigiama skaiciu:"))
slaptas_skaicius=random.randint(1,n)
bandymai=0
netinkami_bandymai=0

while True:
    spejimas=int(input(f"Spekit skaiciu tarp (1 ir {n}):"))
    bandymai+=1
    if spejimas<1 or spejimas>n:
        netinkami_bandymai+=1
        print(f"Netinkamas skaicius. Pasirinkite tarp 1 ir {n}.")
        continue
    if spejimas<slaptas_skaicius:
        print(f"Slaptas skaicius didesnis uz {spejimas} skaiciu")
    elif spejimas>slaptas_skaicius:
        print(f"Slaptas skaicius mazesnis uz {spejimas} skaiciu")
    else:
        print(f"Sveikinu! Jus atspejote skaiciu {slaptas_skaicius} is {bandymai} kartu. Netinkamai pasirinkote {netinkami_bandymai} kartus")
        zaisti_dar_karta = input("Ar norite zaisti dar karta? (T/N):")
        if zaisti_dar_karta.upper()=="N":
            break
        else:
            n=int(input("Pasirinkite teigiama skaiciu:"))
            slaptas_skaicius=random.randint(1,n)
            bandymai=0
            netinkami_bandymai=0