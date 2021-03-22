f=open("sentences.txt","w")
print("Enter text: Type @% when you're done (to exit)\n")
s=""
while s!='@%':
    s=input()
    if s=='@%': continue
    f.write(s+"\n")
f.close()