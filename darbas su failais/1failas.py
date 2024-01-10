f=open('data1.txt','w')

f.write('Pirmas kartas su teksto rasymu. \n')
f.write(str(5))
f.close()

f1=open('data1.txt','r',encoding='UTF-8')
print(f1.readline())
f1.seek(0)
print(f1.readline())
f1.close()