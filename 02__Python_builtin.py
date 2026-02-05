print("\nsection 1")
a=-7.258
print(abs(a))           #7.258
print(round(a))         #-7
b=3+5j
print(abs(b))           #5.830951894845301

c=["True","False",0]
print(all(c))  #False
d=(1,1,2,-1)
print(all(d))  #True
print(any(d))  #True
e={0:"Apple",1:"Orange"}
print(any(e))   #True if all it returns False

print("\nsection 2")

f="I am Good>>å"

print(ascii(f))   #'I am Good>>\xe5'
print(bin(36))    #0b100100
print(bool(5))    #True
print(bytearray(8))   #bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00')
print(bytes(4))       #b'\x00\x00\x00\x00'

print("\nsection 3")
def x():
    a = 5
print(callable(x))    #True

g=97
h=chr(g)
print(h)      #a
i=ord(h)
print(i)    #97

print("\nsection 4")
j = compile('print(55)\nprint(88)', 'test', 'exec')
exec(j)   #55   88

class Person:
  name = "John"
  age = 36
  country = "Norway"

print("\nsection 5")
delattr(Person, 'age')
l = getattr(Person, 'name')
m = hasattr(Person, 'age')
setattr(Person, 'country', 'Iceland')
print(dir(Person))    #['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'country', 'name']
print(divmod(5,2))    #(2,1)
print(l)        #John
print(m)        #False

print("\nsection 6")
x = globals()
print(x)        #{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000018223BC4790>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Users\\HP\\Documents\\PycharmProjects\\pythonProject\\Practicepython\\02__Python_builtin.py', '__cached__': None, 'a': -7.258, 'b': (3+5j), 'c': ['True', 'False', 0], 'd': (1, 1, 2, -1), 'e': {0: 'Apple', 1: 'Orange'}, 'f': 'I am Good>>å', 'x': {...}, 'g': 97, 'h': 'a', 'i': 97, 'j': <code object <module> at 0x0000018223C56550, file "test", line 1>, 'Person': <class '__main__.Person'>, 'l': 'John', 'm': False}
print(x["__file__"])      #C:\Users\HP\Documents\PycharmProjects\pythonProject\Practicepython\02__Python_builtin.py

x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(list(y))      #[(0, 'apple'), (1, 'banana'), (2, 'cherry')]

x = 'print(55)'
eval(x)   #55
y = 'name = "John"\nprint(name)'
exec(y)     #John

print("\nsection 7")

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)
for x in adults:
  print(x)              #18 24 32

print("\nsection 8")
k = format(0.5, '%')
print(k)          #50.000000%

#'<' - Left aligns the result (within the available space)
#'>' - Right aligns the result (within the available space)
#'^' - Center aligns the result (within the available space)
#'=' - Places the sign to the left most position
#'+' - Use a plus sign to indicate if the result is positive or negative
#'-' - Use a minus sign for negative values only
#' ' - Use a leading space for positive numbers
#',' - Use a comma as a thousand separator
#'_' - Use a underscore as a thousand separator
#'b' - Binary format
#'c' - Converts the value into the corresponding unicode character
#'d' - Decimal format
#'e' - Scientific format, with a lower case e
#'E' - Scientific format, with an upper case E
#'f' - Fix point number format
#'F' - Fix point number format, upper case
#'g' - General format
#'G' - General format (using a upper case E for scientific notations)
#'o' - Octal format
#'x' - Hex format, lower case
#'X' - Hex format, upper case
#'n' - Number format
#'%' - Percentage format

mylist = ['apple', 'banana', 'cherry']  #Can't modify frozenset
x = frozenset(mylist)

print(id(x))        #1658457238080
print(hash(x))      #8147147610505916705
x = locals()
print(x)            #{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000018223BC4790>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Users\\HP\\Documents\\PycharmProjects\\pythonProject\\Practicepython\\02__Python_builtin.py', '__cached__': None, 'a': -7.258, 'b': (3+5j), 'c': ['True', 'False', 0], 'd': (1, 1, 2, -1), 'e': {0: 'Apple', 1: 'Orange'}, 'f': 'I am Good>>å', 'x': {...}, 'g': 97, 'h': 'a', 'i': 97, 'j': <code object <module> at 0x0000018223C56550, file "test", line 1>, 'Person': <class '__main__.Person'>, 'l': 'John', 'm': False, 'y': 'name = "John"\nprint(name)', 'name': 'John', 'ages': [5, 12, 17, 18, 24, 32], 'myFunc': <function myFunc at 0x0000018223C1B0A0>, 'adults': <filter object at 0x0000018223C3C970>, 'k': '50.000000%', 'mylist': ['apple', 'banana', 'cherry']}
#help(int)
#n=input("Enter a string")
#print(n)

print("\nsection 9")
def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(x))        #['appleorange', 'bananalemon', 'cherrypineapple']

o=[1,6,2,7,3,5]
print(max(o))     #7
print(min(o))     #1

p=memoryview(b'Hello')
print(p[0])       #72

print("\nsection 10")
mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)    #apple
x = next(mylist)
print(x)    #banana
x = next(mylist)
print(x)    #cherry

q=pow(4,3)
print(q)    #64
r=pow(4, 3, 5)   #(4*4*4)%5
print(r)    #4

print("\nsection 11")
alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
  print(x)    #d c b a

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])        #('a', 'd', 'g')

print("\nsection 12")
a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)
print(x)            #['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

a = (1, 2, 3, 4, 5)
x = sum(a, 7)
y = sum(a)
print(x)        #22
print(y)        #15

print("\nsection 13")
class Person:
  name = "John"
  age = 36
  country = "norway"

x = vars(Person)
print(x)      #{'__module__': '__main__', 'name': 'John', 'age': 36, 'country': 'norway', '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

print(list(x))   #[('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica')]