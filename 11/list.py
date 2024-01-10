txt='5, 9, 6, 8, 1, 9, 4, 1, 8, 4, 5, 6, 8, 41, 8, 1, 19, -5, -15, 25, 85, 69, 26'
# print txt eilutes isvesti liginiu skaiciu eilute
sk=[int(i)for i in txt.split(', ') if int(i)%2==0]
print(sk)