aibeA={1,2,3,4,5}
aibeB={1,2,3,4,5,7,8,11}
aibeC={12,13,14,15}
aibeD={1,2,5,6}

# ar poaibis?
print(f"Ar poaibis? {aibeA.issubset(aibeB)}") #True

# ar virsribis?
print(f"Ar virsribis? {aibeB.issuperset(aibeA)}") #True

# ar skirtingi?
print(f"Ar skirtingi? {aibeC.isdisjoint(aibeB)}") #True

# aibiu sajunga
aibeE=aibeA.union(aibeD)
print(f"Aibiu sajunga aibe A ir aibe D= {aibeE}")

# aibiu sankinrta
aibeF=aibeD.intersection(aibeA)
print(f"Aibes D ir Aibes A sankirta= {aibeF}")

# aibiu skirtumas
aibeG=aibeA.difference(aibeD)
print(f"Aibes A ir Aibes D skirtumas= {aibeG}")

