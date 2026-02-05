thislist=['Apple','Banana','Cherry','Apple', 123, 4.0]

print("\nsection 1")
print(len(thislist))        #6
print(type(thislist))       #<class 'list'>

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

print(thislist[1])      #Banana
print(thislist[-2])     #123
print(thislist[2:4])    #['Cherry', 'Apple']
print(thislist[ :5])    #['Apple', 'Banana', 'Cherry', 'Apple', 123]
print(thislist[-5:-2])  #['Banana', 'Cherry', 'Apple']
if "Apple" in thislist:
    print("Apple is present in list")       #Apple is present in list

print("\nsection 2")

thislist=['Apple','Banana','Cherry','Apple', 123, 4.0]

thislist[1]="Blueberry"       #Replace
print(thislist)             #['Apple', 'Blueberry', 'Cherry', 'Apple', 123, 4.0]
thislist[4:6]=["Durian","Elaichi"]    #Replace
print(thislist)                #['Apple', 'Blueberry', 'Cherry', 'Apple', 'Durian', 'Elaichi']
thislist.insert(3, "CitrusFruit")

print("\nsection 3")
thislist.append("Figs")
print(thislist)     #['Apple', 'Blueberry', 'Cherry', 'CitrusFruit', 'Apple', 'Durian', 'Elaichi', 'Figs']
anotherlist=["Grape","Honey", "ItaPalm"]
thislist.extend(anotherlist)
print(thislist)   ##['Apple', 'Blueberry', 'Cherry', 'CitrusFruit', 'Apple', 'Durian', 'Elaichi', 'Figs', 'Grape', 'Honey', 'ItaPalm']

anothertuple=("Jackfruit", "Kiwis", "Apple")
thislist.extend(anothertuple)
print(thislist)  #['Apple', 'Blueberry', 'Cherry', 'CitrusFruit', 'Apple', 'Durian', 'Elaichi', 'Figs', 'Grape', 'Honey', 'ItaPalm', 'Jackfruit', 'Kiwis', 'Apple']

print("\nsection 4")
thislist.remove("CitrusFruit")
thislist.remove("Apple")     #First Apple from list
print(thislist)         #['Blueberry', 'Cherry', 'Apple', 'Durian', 'Elaichi', 'Figs', 'Grape', 'Honey', 'ItaPalm', 'Jackfruit', 'Kiwis', 'Apple']

thislist.pop()     #Last Apple in list
print(thislist)         #['Blueberry', 'Cherry', 'Apple', 'Durian', 'Elaichi', 'Figs', 'Grape', 'Honey', 'ItaPalm', 'Jackfruit', 'Kiwis']
thislist.pop(2)    #Apple in index 2
print(thislist)     #['Blueberry', 'Cherry', 'Durian', 'Elaichi', 'Figs', 'Grape', 'Honey', 'ItaPalm', 'Jackfruit', 'Kiwis']

print("\nsection 5")
del thislist[6]    #Deleting Honey
print(thislist)     #['Blueberry', 'Cherry', 'Durian', 'Elaichi', 'Figs', 'Grape', 'ItaPalm', 'Jackfruit', 'Kiwis']

thislist.clear()
print(thislist)     #[]

print("\nsection 6")
newlist=["A","E","I","O","U"]
print(newlist)      #['A', 'E', 'I', 'O', 'U']
#del newlist
#print(newlist)

for i in newlist:
    print(i)        #A E I O U

for i in range(len(newlist)):
    print("index: ", i, newlist[i])

"""
index:  0 A
index:  1 E
index:  2 I
index:  3 O
index:  4 U
"""

print("\nsection 7")
j=0
while j < len(newlist):
    print(newlist[j])       #A E I O U
    j=j+1

lis=['Apple','Blueberry', 'Cherry', 'Durian', 'Elaichi', 'Figs', 'Grape', 'Honey', 'ItaPalm', 'Jackfruit', 'Kiwis']
newlis=[]

for x in lis:
  if "a" in x:
    newlis.append(x)
print(newlis)       #['Durian', 'Elaichi', 'Grape', 'ItaPalm', 'Jackfruit']

print("\nsection 8")

newlis=[x for x in lis if "a" in x]
print(newlis)           #['Durian', 'Elaichi', 'Grape', 'ItaPalm', 'Jackfruit']
nlis=[x for x in newlis if x != "Grape"]
print(nlis)             #['Durian', 'Elaichi', 'ItaPalm', 'Jackfruit']

alist = [x for x in range(10) if x < 5]
print(alist)            #[0, 1, 2, 3, 4]
blist = [x.upper() for x in nlis]
print(blist)            #['DURIAN', 'ELAICHI', 'ITAPALM', 'JACKFRUIT']

print("\nsection 9")

clist = ["orange", "mango", "kiwi", "pineapple", "banana"]
clist.sort()
print(clist)        #['banana', 'kiwi', 'mango', 'orange', 'pineapple']
clist.sort(reverse=True)
print(clist)        #['pineapple', 'orange', 'mango', 'kiwi', 'banana']
clist.reverse()
print(clist)        #['banana', 'kiwi', 'mango', 'orange', 'pineapple']

cpylist=clist.copy()
print("THis is copied list", cpylist)       #THis is copied list ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
dlist=list(lis)
print("Another copy method", dlist)     #Another copy method ['Apple', 'Blueberry', 'Cherry', 'Durian', 'Elaichi', 'Figs', 'Grape', 'Honey', 'ItaPalm', 'Jackfruit', 'Kiwis']

print("\nsection 10")
elist=clist+dlist
print(elist)        #['banana', 'kiwi', 'mango', 'orange', 'pineapple', 'Apple', 'Blueberry', 'Cherry', 'Durian', 'Elaichi', 'Figs', 'Grape', 'Honey', 'ItaPalm', 'Jackfruit', 'Kiwis']

flist=["a","b","c","a","c"]
glist=[1,2,3]
flist.extend(glist)
print(flist)        #['a', 'b', 'c', 'a', 'c', 1, 2, 3]

num=flist.count("a")
print(num)      #2
ind=flist.index("b")
print(ind)      #1

print("\nsection 11")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)        #('apple', 'kiwi', 'cherry')

print("\nsection 12")
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)    #('apple', 'banana', 'cherry', 'orange')

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

print("\nsection 13")
(green, yellow, *red) = fruits

print(green)        #apple
print(yellow)       #banana
print(red)          #['cherry', 'strawberry', 'raspberry']

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)      #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')


#Arrays