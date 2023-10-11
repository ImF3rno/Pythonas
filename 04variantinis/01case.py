#ivedu savaites diena skaiciumi 5 paraso - penktadienis

diena=int(input('Kokia savaites diena...'))
viskasOk=True
match diena:
    case 1:
        txt='Pirmadienis'
    case 2:
        txt='Antradienis'
    case 3:
        txt='Treciadienis'
    case 4:
        txt='Ketvirtadienis'
    case 5:
        txt='Penktadienis'
    case 6:
        txt='Sestadienis'
    case 7:
        txt='Sekmadienis'
    case _:
        print('Blogai ivesti duomenys')
        viskasOk=False

if viskasOk:
    print(f'{diena}-{txt}')