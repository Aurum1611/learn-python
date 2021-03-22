num=int(input("Enter a number: "))
for i in range(1,num+1):
    if i%10==0:
        continue
    elif i>=100:
        break
    print(i)
