def get_value(z):
    s = 0
    for i in range(0, z + 1):
        s = s + 2 ** i
    return s


n = int(input("Enter the number of bits: "))
print(n, 'bits can store a max value of:', get_value(n))
