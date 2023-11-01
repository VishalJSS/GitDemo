a = 200
b = 33
c = 500
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")      #a is greater than b

#AND, OR and NOT
if a > b and c > a:
  print("Both conditions are True")      #Both conditions are True

if a > b or a > c:
  print("At least one of the conditions is True")       #At least one of the conditions is True

if not b > a:
  print("b is NOT greater than a")      #b is NOT greater than a

if a > b:
    pass

i = 1
while i < 6:
  print(i)          # 1 2 3
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)          # 1 2 4 5 6

for x in range(6):
  print(x)          #0 1 2 3 4 5
print("\n")

for x in range(2, 6):
  print(x)      # 2 3 4 5
print("\n")

for x in range(2, 30, 3):
  print(x)      # 2 5 8 11 14 17 20 23 26 29

def my_function():
    print("Hello function")     #Hello function
my_function()

def my_function(fname, lname):
    print(fname+" "+lname)          #Nick Jonas
my_function("Nick","Jonas")

#Arbitrary Array
def my_function(*kids):
  print("The youngest child is " + kids[2])     #The youngest child is Linus
my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)      #The youngest child is Linus
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#If no of argument unknown
def my_function(**kid):
  print("His last name is " + kid["lname"])     #His last name is Refsnes
my_function(fname = "Tobias", lname = "Refsnes")

#Default
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")       #I am from Sweden
my_function("India")        #I am from India
my_function()               #I am from Norway

def my_function(x):
  return 5 * x              #15
print(my_function(3))

def my_function(food):
  for x in food:
    print(x)        #apple banana cherry
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

x = lambda a : a + 10
print(x(5))     #15

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))       #13

def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))            #33

#Method Resolution Order
class A:
    id=1
class B:
    id=2
class C:
    id=3
class D(A,C,B):
    pass

print(D.id)         #1

class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)     #5

#Parent
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name + " I am {} old".format(self.age))

p1 = Person("John", 36)
print(p1.name)              #John
print(p1.age)               #36
p1.myfunc()                 #Hello my name is John I am 36 old

#Child
class Student(Person):
    pass
x= Student("James", 26)
x.myfunc()          #Hello my name is James I am 26 old

#Inheritance
class Student(Person):
    def __init__(self, name, age):
        Person.__init__(self,name,age)
x=Student("Jonas",56)
x.myfunc()          #Hello my name is Jonas I am 56 old

class Student(Person):
  def __init__(self, name, age):
    super().__init__(name, age)
    self.graduationyear = 2016
x=Student("Mike", 46)
print(x.graduationyear)         #2016

x = 300
def myfunc():
  x = 200
  print(x)      #200
myfunc()
print(x)        #300

print("\n")

x=200
def myfunc():
  global x
  x = 300
myfunc()
print(x)        #300