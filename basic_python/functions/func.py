def avg(a,b):
    c=(a+b)/2
    return c

numl=[float(i) for i in input("Enter two numbers separated by spaces: ").split()]
print("The average of",numl[0],"and",numl[1],"is:",avg(numl[0],numl[1]))