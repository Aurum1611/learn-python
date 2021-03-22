from _functools import reduce
numl=[1,2,3,4,5]\

res=reduce(lambda x,y:x+y,numl)
print(int(res))