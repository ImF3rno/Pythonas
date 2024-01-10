# sukuriama kelias eilutes sarasu. Nuskaityti juos ir sudeti i atskirus sarasus

def sukurimas():
    with open('data3.txt','w',encoding='UTF-8') as f:
        f.write('10 25 14 25 47 36\n')
        f.write('1 5 4 8\n')
        f.write('5 8 7 6 9 5 44 1 2 5\n')
        f.write('10 25 14 25 47 36\n')
        f.write('1 5 4 8\n')
        f.write('5 8 7 6 9 5 44 1 2 5\n')

def skaitymas():
    with open('data3.txt','r',encoding='UTF-8') as f:
        txt=[]
        while True:
            eil=f.readline()
            if eil:
                txt.append(eil)
            else:
                break
        return txt

sukurimas()
visas=skaitymas()
print(visas)
skaiciai=[]
for eil in visas:
    eilSk=[int(x) for x in eil.split(' ')]
    skaiciai.append(eilSk)
print(skaiciai)

# for i in eilSk:
#     print(skaiciai[i])