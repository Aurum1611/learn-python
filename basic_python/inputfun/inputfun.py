# name = input("Enter your name: ")
# marks = float(input("Enter the marks scored by you: "))
# print(name, marks)

"""
lt=[x for x in input("Enter three numbers separated by spaces: ").split()]

This is how the instructor did it. It gives the same output with extra code
so basically it's useless if you want to create a list containing strings.
It's a necessity though if you want the entered values to be type casted.
"""

# lt = input("Enter three numbers separated by spaces: ").split()
lt = [float(x) for x in input("Enter marks scored in three subjects (Separated by spaces): ").split()]
print(lt)
print(type(lt))
print(lt[1])
print(type(lt[1]))

a, b, c = [int(x) for x in input("Enter three numbers: ").split()]
print(a, b, c, sep=",")

a = [int(x) for x in input("Enter three numbers: ").split()]
print(a)
