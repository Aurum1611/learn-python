num = int(input("Enter a number: "))
primeFlag = True
for i in range(2, num - 1):
    if num % i == 0:
        primeFlag = False
if primeFlag:
    print("It's a prime number.")
else:
    print("It isn't a prime number.")
