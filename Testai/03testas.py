import sys

bylu_sarasas=['Testai/duom1.txt','Testai/duom2.txt','Testai/duom 3.txt','Testai/duom4.txt']
bylu_klaidos=[]
bylu_info=[]
try:
    for byla in bylu_sarasas:
        try:
            f=open(byla,'r')
            bylu_info.append(f.read())
        except Exception as ex:
            bylu_klaidos.append(byla)
            sys.exit()
finally:
    f=open('loog.txt','w')
    for i in bylu_info:
        f.write(i)
        f.write("\n")
    f.write(str(bylu_klaidos))
    f.close()