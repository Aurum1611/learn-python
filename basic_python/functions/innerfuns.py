def disp(name):
    print("No to hello world.")
    def msg():
        return "You're in the inner function now "+name
    return "I want to tell you that:\n"+msg()

print(disp("Watari"))