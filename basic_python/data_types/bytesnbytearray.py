lst = [12, 45, 99, 77, 124, 234]
print(type(lst))
b = bytes(lst)
print(type(b))
ba = bytearray(lst)
print(type(ba))
ba.append(34)
ba[5] = 12
