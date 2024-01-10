skaicius=int(input('Iveskite skaiciu:'))
skaiciusZodziais=str(skaicius)[::-1]
galimybes={
    '0':'-','1':'*','2':'**','3':'***','4':'****','5':'*****','6':'******','7':'*******','8':'********','9':'*********',
}
for i in skaiciusZodziais:
    if i in galimybes:
        print(galimybes[i])