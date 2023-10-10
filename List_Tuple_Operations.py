thislist=['Apple','Banana','Cherry','Apple', 123, 4.0]

print(len(thislist))
print(type(thislist))

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

print(thislist[1])
print(thislist[-2])
print(thislist[2:4])
print(thislist[ :5])
print(thislist[-5:-2])
if "Apple" in thislist:
    print("Apple is present in list")



thislist=['Apple','Banana','Cherry','Apple', 123, 4.0]

thislist[1]="Blueberry"       #Replace
print(thislist)
thislist[4:6]=["Durian","Elaichi"]    #Replace
print(thislist)
thislist.insert(3, "CitrusFruit")

thislist.append("Figs")
print(thislist)
anotherlist=["Grape","Honey", "ItaPalm"]
thislist.extend(anotherlist)
print(thislist)

anothertuple=("Jackfruit", "Kiwis", "Apple")
thislist.extend(anothertuple)
print(thislist)

thislist.remove("CitrusFruit")
thislist.remove("Apple")     #First Apple from list
print(thislist)

thislist.pop()     #Last Apple in list
print(thislist)
thislist.pop(2)    #Apple in index 2
print(thislist)

del thislist[6]    #Deleting Honey
print(thislist)

thislist.clear()
print(thislist)

newlist=["A","E","I","O","U"]
print(newlist)
#del newlist
#print(newlist)

for i in newlist:
    print(i)

for i in range(len(newlist)):
    print("index: ", i, newlist[i])

j=0
while j < len(newlist):
    print(newlist[j])
    j=j+1

lis=['Apple','Blueberry', 'Cherry', 'Durian', 'Elaichi', 'Figs', 'Grape', 'Honey', 'ItaPalm', 'Jackfruit', 'Kiwis']
newlis=[]

for x in lis:
  if "a" in x:
    newlis.append(x)
print(newlis)

newlis=[x for x in lis if "a" in x]
print(newlis)
nlis=[x for x in newlis if x != "Grape"]
print(nlis)

alist = [x for x in range(10) if x < 5]
print(alist)
blist = [x.upper() for x in nlis]
print(blist)

clist = ["orange", "mango", "kiwi", "pineapple", "banana"]
clist.sort()
print(clist)
clist.sort(reverse=True)
print(clist)
clist.reverse()
print(clist)

cpylist=clist.copy()
print("THis is copied list", cpylist)
dlist=list(lis)
print("Another copy method", dlist)

elist=clist+dlist
print(elist)

flist=["a","b","c","a","c"]
glist=[1,2,3]
flist.extend(glist)
print(flist)

num=flist.count("a")
print(num)
ind=flist.index("b")
print(ind)

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)