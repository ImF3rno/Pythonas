# try:
#     sk=int(input("Iveskite skaiciu: "))
# except ValueError:
#     print("Blogai ivesti duomenys.")
#     sk=int(input("Iveskite skaiciu: "))

while True:
    try:
        sk=int(input("Iveskite skaiciu: "))
        break
    except ValueError as ex:
        print(f"Blogai ivesti duomenys. Klaida: {ex}")

print(f'sk={sk}')