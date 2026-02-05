a='Stringisgood'
lst=[]
for i in a:
    if i not in lst:
        lst.append(i)
print(lst)
dct={}
count=0
for k in a:
    if k not in dct:
        dct[k]=1
    else:
        dct[k]=dct[k]+1
print(dct)