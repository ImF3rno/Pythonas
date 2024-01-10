txt='Mano batai buvo du, bet kazkas atsitiko - nerandu'

print(len(txt))
print(txt[-1])

# kiek yra zodziu sakinyje
kiekZodziu=txt.count(' ')
print(kiekZodziu)

print(txt.capitalize())

print(txt.upper())
print(txt.lower())

print(txt.islower())
print(txt.isupper())

print(txt.find('a'))
print(txt.find('a',5,15))
print(txt.find('ch',5,15))

# t='123 abc 456'
# t1='abcd'
# t4='     '
# print(t.isalnum())
# print(t1.isalnum())
# print(t.isalpha())

str = '1111He1lo1111'
print(str.strip('1'))

t='Man patinka coco cola'
print(t.replace('coco','Pepsi'))

print(ord('a'))
print(chr(261))