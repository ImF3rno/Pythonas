#visus skaicius nuo 1 iki n, jei 13 uzbaigti

n=int(input('n='))
for i in range(1,n):
    if i==13:
        break
    print(i,end=(', '))
else:
    print('\nCiklas uzbaigtas')
print('Kiti sakiniai')