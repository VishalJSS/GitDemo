#The values True and 1 are considered the same value in sets, and are treated as duplicates
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)    #{True, 2, 'apple', 'cherry', 'banana'}

for x in thisset:
  print(x)    #True 2 apple cherry banana

print("banana" in thisset)    #True

thisset.add("orange")
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)    #{True, 2, 'pineapple', 'papaya', 'cherry', 'banana', 'mango', 'orange', 'apple'}

thisset.remove("papaya")
thisset.discard("mango")
thisset.pop()   #Removes something random
print(thisset)    #{2, 'pineapple', 'cherry', 'banana', 'orange', 'apple'}
thisset.clear()

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)     #{1, 2, 3, 'c', 'b', 'a'}

set1.update(set2)
print(set1)     #{1, 2, 3, 'c', 'b', 'a'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)    #{'apple'}

z=x.intersection(y)
print(z)    #{'apple'}

x.symmetric_difference_update(y)
print(x)    #{'google', 'microsoft'}

z = x.symmetric_difference(y)
print(z)    ##{'apple'}

x.add("d")
print(x)    #{'d', 'google', 'microsoft'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z=x.difference(y)
print(z)    #{'cherry', 'banana'}
y.difference_update(x)
print(y)    #{'google', 'microsoft'}

x.isdisjoint(y)
print(x)    #{'cherry', 'banana', 'apple'}

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)      #True
z = y.issubset(x)
print(z)      #True

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)     #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(thisdict["brand"]) #Ford

#Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "colors": ["red", "white", "blue"]
}
print(thisdict)     #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'colors': ['red', 'white', 'blue']}
print(len(thisdict))    #4

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)     #{'name': 'John', 'age': 36, 'country': 'Norway'}
print(thisdict.get("name"))   #John
x=thisdict.keys()
y=thisdict.values()
z=thisdict.items()
print(x)    #dict_keys(['name', 'age', 'country'])
print(y)    #dict_values(['John', 36, 'Norway'])
print(z)    #dict_items([('name', 'John'), ('age', 36), ('country', 'Norway')])
thisdict["color"] = "White"
print(thisdict)   #{'name': 'John', 'age': 36, 'country': 'Norway', 'color': 'White'}
if "color" in thisdict:
  print("color is present")     #color is present
thisdict.update({"color" : "Black"})
print(thisdict)     #{'name': 'John', 'age': 36, 'country': 'Norway', 'color': 'Black'}

thisdict.pop("age")
print(thisdict)   #{'name': 'John', 'country': 'Norway', 'color': 'Black'}

thisdict.popitem()  #Removes last inserted item
print(thisdict)   #{'name': 'John', 'country': 'Norway'}

thisdict.clear()
print(thisdict)   #{}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(x)            #To get keys        brand   model   year
  print(thisdict[x])  #To get values      Ford    Mustang   1964

for x in thisdict.values():
  print(" ", x)

"""
  Ford
  Mustang
  1964
"""
for x in thisdict.keys():
  print(" ", x)
"""
  brand
  model
  year
"""
for x, y in thisdict.items():
  print(x, y)
"""
brand Ford
model Mustang
year 1964
"""
mydict = thisdict.copy()
print(mydict)   #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

mydict = dict(thisdict)
print(mydict)   #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

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

print(myfamily["child2"]["name"])     #Tobias

x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)     #{'key1': 0, 'key2': 0, 'key3': 0}

x = thisdict.setdefault("color", "white")
print(x)    #white