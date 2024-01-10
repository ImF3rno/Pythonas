aibeA={1,2,3,4,5}
aibeB={1,2,3,4,5,7,8,11}
aibeC={12,13,14,15}
aibeD={-1,1,2,5,6}

# aibeA.update(aibeB)
# print(aibeA)

# salinimas su klaida
aibeA.remove(1)
print(aibeA)
print("=-=-=-=-=-=-=-=")

# salinimas be klaidos
aibeA.discard(12)
print(aibeA)
print("=-=-=-=-=-=-=-=")

# grazina pasalinta reiksme
kazkas=aibeA.pop()
print(kazkas)
print("=-=-=-=-=-=-=-=")

# visos aibes isvalymas
aibeC.clear()
aibeC.add(5)
print(aibeC)