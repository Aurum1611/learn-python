def disp(name):
    def msg():
        return "You're in the inner function now "+name
    return msg

fun=disp("Akane")
print(fun())