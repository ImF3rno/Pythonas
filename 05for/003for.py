#Petriukas turi x euru ir y centu.  Senelis kas dien duoda po a centu. Atspausdinkite visu metu ataskaita kas diena kaip keitesi petriuko santaupos
# 15eur 28ct. Senelis duoda 50ct
# 1 diena tures 15eur. 78ct.
# 2 diena tures 16eur. 28ct.
#..................................
# 365 diena tures......

euraiPetriukas = int(input('Kiek euru turi Petriukas '))
centaiPetriukas = int(input('Kiek centu turi Petriukas '))
centaiSenelis = int(input('Kiek euru turi Senelis '))
visoCentaiPetriukas = euraiPetriukas*100 + centaiPetriukas
for i in range(1, 366):
    visoCentaiPetriukas += centaiSenelis
    print(f'{i}-a diena Petriukas tures {visoCentaiPetriukas//100}euru ir {visoCentaiPetriukas%100} centu')
