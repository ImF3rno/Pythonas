# apskaiciuoti rez=100/sk

cikasVeikia=True

while cikasVeikia:
    try:
        sk=int(input("Iveskite skaiciu: "))
        rez=100/sk
        cikasVeikia=False
    except ValueError as ex:
        print(f"Blogai ivesti duomenys. Klaida: {ex}")
    except ZeroDivisionError as ex:
        print(f'Dalyba is 0 negalima. Klaida: {ex}')
    else:
        print("Panasu, kad viskas gerai")
    finally:
        print("Man dzin ar viskas buvo gerai")

print(f'rez={rez}')