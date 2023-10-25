skaicius=int(input('Iveskite kiek skaiciu?'))
suma=0
dabartinis=7
for i in range(skaicius):
    suma+=dabartinis
    dabartinis=dabartinis*10+7
print(suma)