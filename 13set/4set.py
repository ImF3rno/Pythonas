import time

sarA=list(range(0,10000,2))
sarB=list(range(2500,16000,3))
sarC=list(range(1000,30000,7))

# def fun(*args):
#     sar=[]
#     for i in args:
#         for j in i:
#             if j not in sar:
#                 sar.append(j)
#     return sar

pradzia1=time.time()
aibeA=set(sarA)
saibeB=aibeA.union(set(sarB),set(sarC))
pabaiga1=time.time()-pradzia1

print(pabaiga1)

# pradzia2=time.time()
# fun(sarA,sarB,sarC)
# pabaiga2=time.time()-pradzia2

# print(pabaiga2)