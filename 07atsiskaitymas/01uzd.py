visasIlgis=float(input('Kalamo vinies ilgis?='))
ikalimas=float(input('Kiek ikala su vienu smugiu?='))
smugiu_skaicius=0
for i in range(int((visasIlgis/ikalimas)+1)):
    visasIlgis=visasIlgis-ikalimas
    smugiu_skaicius=smugiu_skaicius+1
    if visasIlgis>0:
        print(f'TUK! {smugiu_skaicius} dar liko {round(visasIlgis,2)} cm')
    else:
        print(f'TUK! {smugiu_skaicius} ikaltas.')
        break
