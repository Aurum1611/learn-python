s1 = "I'm awesome. I'm awesome. "
print(s1 * 5, "\n")

s2 = """For every action,
there's always an equal and opposite
reaction
    - Issae Newtie"""
print(s2)

print(len(s2))

print(s1[0:5])
print(s1[-3:-1] + '\n')

print(s1[8:0:-1])
print(s1[::-1])
print(s1[::2])
print(s1[::3])

print(s1.rstrip())

print('find', s2.find('ua'))
print(s1.count(' '))
print(s1.replace("awesome", "amazing", 1))

print(s1[:8], len(s1[:8]), "\n")

s3 = 'mINATA yAMAMOTO'
print(s3.upper())
print(s3.lower())
print(s3.capitalize())
print(s3.title())
