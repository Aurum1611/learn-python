def decor(fun):
    def inner():
        res = fun()
        return res * 2

    return inner


def numRet():
    return 7


resFun = decor(numRet)
print(resFun())
