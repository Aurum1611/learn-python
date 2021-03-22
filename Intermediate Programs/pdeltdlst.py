lst=[x for x in range(1,10) if x%2==0]
rst=[x for x in range(1,10) if x%2!=0]

'''
res=[]
for i in range(len(lst)):
    res.append(lst[i]*rst[i])
'''
res=[lst[i]*rst[i] for i in range(len(lst))]

print(res)