import math

class TrikampioKlaida(Exception):
    '''Viena is trikampio klaidu'''

def trik_plotas(a,b,c):
    if(a<=0 or b<=0 or c<=0):
        raise TrikampioKlaida("Krastines turi buti didesnes nei 0")
    pusperimetris=(a+b+c)/2
    s=math.sqrt(pusperimetris*(pusperimetris-a)*(pusperimetris-b)*(pusperimetris-c))
    return s

tri1=trik_plotas(5,8,4)
print(tri1)
try:
    tri2=trik_plotas(-2,10,10)
except TrikampioKlaida as ex:
    print(f"klaida: {ex}")
else:
    print(tri2)