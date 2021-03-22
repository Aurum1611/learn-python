def calc(a,b):
    return a+b, a-b, a*b, a/b

print(calc(12,3))

for i in calc(12,3):
    print(i)