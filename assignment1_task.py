lst=[3,5,[3,56],3,[3,7,'zen',4.6],'guvi',5,2,'pit']
sublistcnt=0
max=0
for z in lst:
    if isinstance(z,list):
        sublistcnt+=1
        if max < len(z):
            max=len(z)
            index=lst.index(z)
print(sublistcnt)
print(lst[index])
print(index)
print([index][0])
