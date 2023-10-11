#ivedu skaiciu 5 
#skaicius 5!=5*4*3*2*1
import math

skaicius=int(input('Iveskite skaiciu='))
fak=1
print(f'{skaicius}!=',end='')
for i in range(0,skaicius+1):
    math.factorial(skaicius)
    if i!=skaicius:
        print(f'{i}',end='*')
    else:
        print(f'{i}',end='=')
print(f'{math.factorial(skaicius)}')