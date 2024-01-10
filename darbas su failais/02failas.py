try:
    f=open('data2.txt','w')
    f.write('Belekas \n')
    f.write('Dar vienas \n')
finally:
    f.close()

with open('data2.txt','a',encoding='UTF-8')as f1:
    f1.write('Tratata \n')
    f1.write('Tratata \n')
print('Tratata')