m=[5,8,9,7,9,4,-1]
print(m)
m.append(-111) #ideda i gala
print(m)
m.insert(1,-8888) #ideda i norima vieta
print(m)

kiek9=m.count(9) #suranda kuris yra eileje
print(kiek9)

m.sort(reverse=True) #mazejanciai
print(m)

m.sort() #didejanciai
print(m)

txt=['a','abc','ab','acb','acb','cad','f']
txt.sort()
print(txt)
txt.sort(key=len)
print(txt)

txt.sort(key=len,reverse=True)
print(txt)

didziausias=max(m)
maz=min(m)

print(m)
m.pop()
print(m)

print(m)
m.pop(2)
print(m)