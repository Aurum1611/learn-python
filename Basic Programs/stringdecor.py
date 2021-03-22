def howareyou(fun):
    def inner(n):
        res=fun(n)
        return res+"\nHow are you?"
    return inner

@howareyou
def hello(name):
    return "Hello! "+name

print(hello("Eren"))
