txt='Man ą ė šlabai pįšųatinka rūų9ytaięęėįs ankstiąą keęėįltis ir eiti i mokykla'
lt=('ąčęėįšųūžĄČĘĖĮŠŲŪŽ')
kiek=0
for i in txt:
    if i in lt:
        kiek+=1
print(f'Sakinyje "{txt}" yra {kiek} LT simboliu')