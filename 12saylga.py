#koks 'veikiantis' p 1<=p<=10
#koks 'neveikiantis'?

def ivedimas():
    p=int(input('p= '))
    if not(1<=p<=10):
        print('Netinkamas balas')
        return ivedimas()
    else:
       return p

paz=ivedimas()
print(paz)