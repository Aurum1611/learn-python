lst=[5,2,3,7,9,13,23,21]
rst=[11,2,12,13,7,45,5,23,44]
res=[]

'''for i in lst:
    if i in rst:
        res.append(i)'''

res=[i for i in lst if i in rst]

print(res)