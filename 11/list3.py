sar1=[2, 4, -5, 6, -8, 4, 7, 5]
sar2=[-1, -2, 4, 3, 2.5, -2, 5]
sarNum1=[]
for x in sar1:
    for y in sar2:
        sum0=x+2*y
        if sum0==0:
            sarNum1.append([x, y])
print(sarNum1)

sar0=[[x,y] for x in sar1 for y in sar2 if x+2*y==0]
print(sar0)