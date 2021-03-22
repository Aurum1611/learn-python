def fact(num):
    if num==1:
        return 1
    f=num*fact(num-1)
    return f

num=int(input("Enter a number of which you want to find the factorial: "))
print(str(num)+"! = ",fact(num))