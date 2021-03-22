class Duck:
    def talk(self):
        print("Quack Quack")

class Human:
    def talk(self):
        print("Hello! How are you?")

def ducktyping(obj):
    obj.talk();

d=Duck()
h=Human()

ducktyping(d)
ducktyping(h)