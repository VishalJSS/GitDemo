a=-7.258
print(abs(a))
print(round(a))
b=3+5j
print(abs(b))

c=["True","False",0]
print(all(c))  #False
d=(1,1,2,-1)
print(all(d))  #True
print(any(d))  #True
e={0:"Apple",1:"Orange"}
print(any(e))   #True if all it returns False

f="I am Good>>å"

print(ascii(f))
print(bin(36))
print(bool(5))
print(bytearray(8))
print(bytes(4))

def x():
    a = 5
print(callable(x))

g=97
h=chr(g)
print(h)
i=ord(h)
print(i)

j = compile('print(55)\nprint(88)', 'test', 'exec')
exec(j)

class Person:
  name = "John"
  age = 36
  country = "Norway"

delattr(Person, 'age')
l = getattr(Person, 'name')
m = hasattr(Person, 'age')
setattr(Person, 'country', 'Iceland')
print(dir(Person))
print(divmod(5,2))
print(l)
print(m)

x = globals()
print(x)
print(x["__file__"])

x = ('apple', 'banana', 'cherry')
y = enumerate(x)

x = 'print(55)'
eval(x)
y = 'name = "John"\nprint(name)'
exec(y)

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)
for x in adults:
  print(x)

k = format(0.5, '%')
print(k)

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

print(id(x))
print(hash(x))
x = locals()
print(x)
#help(int)
#n=input("Enter a string")
#print(n)

def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(x))

o=[1,6,2,7,3,5]
print(max(o))
print(min(o))

p=memoryview(b'Hello')
print(p[0])

mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)
x = next(mylist)
print(x)
x = next(mylist)
print(x)

q=pow(4,3)
print(q)
r=pow(4, 3, 5)   #(4*4*4)%5
print(r)

alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
  print(x)

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])

a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)
print(x)

a = (1, 2, 3, 4, 5)
x = sum(a, 7)
y = sum(a)
print(x)
print(y)

class Person:
  name = "John"
  age = 36
  country = "norway"

x = vars(Person)
print(x)

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

print(list(x))