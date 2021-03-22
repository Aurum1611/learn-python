import sys

numl=sys.argv
pd=1
i=0
while i<(len(numl)-1):
    i+=1
    pd*=int(numl[i])
print("Product is:",pd)