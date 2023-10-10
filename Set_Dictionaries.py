#The values True and 1 are considered the same value in sets, and are treated as duplicates
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

for x in thisset:
  print(x)

print("banana" in thisset)

thisset.add("orange")
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset.remove("papaya")
thisset.discard("mango")
thisset.pop()   #Removes something random
print(thisset)
thisset.clear()

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)

z=x.intersection(y)
print(z)

x.symmetric_difference_update(y)
print(x)

z = x.symmetric_difference(y)
print(z)

x.add("d")
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z=x.difference(y)
print(z)
y.difference_update(x)
print(y)

x.isdisjoint(y)
print(x)

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
z = y.issubset(x)
print(z)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])

#Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(len(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
print(thisdict.get("name"))
x=thisdict.keys()
y=thisdict.values()
z=thisdict.items()
print(x)
print(y)
print(z)
thisdict["color"] = "White"
print(thisdict)
if "color" in thisdict:
  print("color is present")
thisdict.update({"color" : "Black"})
print(thisdict)

thisdict.pop("age")
print(thisdict)

thisdict.popitem()  #Removes last inserted item
print(thisdict)

thisdict.clear()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(x)            #To get keys
  print(thisdict[x])  #To get values

for x in thisdict.values():
  print(" ", x)

for x in thisdict.keys():
  print(" ", x)

for x, y in thisdict.items():
  print(x, y)

mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])

x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

x = thisdict.setdefault("color", "white")
print(x)