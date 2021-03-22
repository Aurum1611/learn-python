d1 = {1: "Jonhy", 2: "Saitama", 3: "Hinata", 4: "Watari"}
print(type(d1))
print(d1, "\n")

print(d1.items())
print(d1.keys())
print(d1.values())

for i in d1.items():
    print(i)

print("\n" + d1[2])
del d1[2]
print(d1.items())
