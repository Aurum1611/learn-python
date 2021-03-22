def gen(x,y):
    while x<y:
        yield x
        x+=2

res=list(gen(20,35))
print(res)