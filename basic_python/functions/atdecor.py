def decorator(fun):
    def inner():
        res=fun()
        return res*2
    return inner

@decorator
def numRet():
    return 7

print(numRet())