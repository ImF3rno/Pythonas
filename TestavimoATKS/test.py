while True:
    try:
        f=open("TestavimoATKS/duom1.txt", "r")
        break
    except ValueError as ex:
        print(f"Blogai ivesti duomenys. Klaida: {ex}")
        
print(f.read())