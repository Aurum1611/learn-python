lst=["India","Japan","USA"]
print(lst)
lst.append("Germany")
print(lst)
del(lst[2])
print(lst)
lst.insert(2, "UK")
print(lst,"\n")

myset={"Tokyo","Berlin","Nairobi"}
print(myset)
myset.update(["Helsinki"])
print(myset)
myset.remove("Tokyo")
print(myset)
myset.update(["Rio"])
print(myset)
