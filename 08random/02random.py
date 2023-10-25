# Zirkles=Z
# Akmenukas=A
# Popierius=P

import random

zaidejas=str(input('Pasirinkite [A/Z/P]'))
pasirinkimai=random.choice(['A','Z','P'])
if zaidejas==pasirinkimai:
    print('Lygesios!')
elif zaidejas=="A" and pasirinkimai=="Z" or zaidejas=="Z" and pasirinkimai=="P" or zaidejas=="P" and pasirinkimai=="A":
    print('Zaidejas laimi!')
else:
    print('Zaidejas pralaimi!')
print(pasirinkimai)