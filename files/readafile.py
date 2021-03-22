import os,sys,math

if os.path.isfile("activities.txt"):
    f=open("activities.txt","r")
    s=f.read()
    print(s)
    f.close()
else:
    print("File doesn't exist")
    sys.exit()
print("Extra text.",math.pi)