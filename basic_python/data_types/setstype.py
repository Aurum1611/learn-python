s = {10, 20, 30, 40, 'xyz', 'abc', "ABC", "XYZ"}
print(s, "\n")
s.update([10, 20, 77, 33, 22, 33])
print(s)
print(type(s), "\n")

r = range(2, 19, 3)
for i in r:
    print(i)

f = frozenset(s)
print(type(f))
