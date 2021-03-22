l1 = [20, 21.0, 29.317, "Waterfall Yakooza"]
print(l1)
print(l1[3])
print(len(l1))
print(l1[1:3], "\n")

l1.append(71)
l1.append("Shinzuke Nishikami")
l1.remove(21.0)
del (l1[2])
print(l1, "\n")

# l1.clear()

l1.remove("Shinzuke Nishikami")
l1.append(-21)
l1.append(-31.221)

print(max(l1))
print(min(l1))
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1, "\n")

l2 = [31]
print(type(l2))
print(l2)

t1 = (90, 51.35, 57.80, 13.09, "xyz", "ahc", 'ABC', 'XYZ')
print(t1)
print(t1.index(13.09))
print(t1[5])
print(t1 * 2)
