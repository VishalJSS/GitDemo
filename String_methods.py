r="This can be rough multiple times"
print(r.capitalize())
print(r.casefold())
print(r.center(80))
print(r.count('t'), r.count('e'))
print(r.encode())
print(r.endswith('s'))
print(r.startswith('T'))
print(r.expandtabs(20))
print(r.find('e'))
s={"t":"something", "u":"Nothing"}
print('{t}{u}'.format_map(s))
print(r.index('b'))
v=["Victory", "32573", "@#$", "treat", 128, "4.0", 6, " space"]
print(v[0].isalpha())
print(v[5].isdecimal())
print(v[1].isdigit())
print(v[3].isdigit())
print(v[1].isnumeric())
print(v[3].islower())
print(v[3].isupper())
#print(v[4].isascii())
#A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
print(v[0].isidentifier())
print(v[7][0].isspace())
w="This is to check\n"
print(w.isprintable())
print(w.istitle())
print(v[0].istitle())
print(w.join(s))
print(r.ljust(60,"0"))
print(r.rjust(60,"0"))
x="      Testing     "
print(x.lstrip())
print(x.rstrip())
y = ",,,,,ssaaww.....banana"
print(y.lstrip(",.asw"))
mytable=str.maketrans("T","B")
print(x.translate(mytable))

txt = "Good night Sam!"
x = "Sam"
y = "Joe"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(mytable)    #Ascii code number is shown with relevant replacement numbers
print(txt.translate(mytable))

x="abcdefghijklmnopqrstuvwxyz"
y="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mytable=str.maketrans(x,y)
print(mytable)

print(txt.partition("night"))
print(txt.partition("midnight"))

#Replace
pat = "one one was a race horse, two two was one too."
x = pat.replace("one", "three", 2)
print(x)

#Index of element last occurence
z="It is too late to obey the orders now"
element=z.rfind("o")
print (element)
limit=z.rfind("o", 1, 12)
print(limit)
change=z.rindex("o", 1, 12)
print(change)

#string.rsplit(separator, maxsplit)

lis="Apple, Banana, Cherry"
li=lis.rsplit( ',')
print(li)
maxsplit=lis.rsplit(',', 1)
print(maxsplit)

txt="Welcome to the Jungle of India"
res=txt.split()
print(res)
lim=txt.split(" ", 3)
print(lim)
txt="hello,i,am,paul"
fin=txt.split(",")
print(fin)

#splitlines
txt="I am very Happy\nProud of your achievements"
first=txt.splitlines()
print(first)
second=txt.splitlines(True)
print(second)

txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
y = txt.startswith("Hel")
print(x)
print(y)

txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)

txt="i AM RIGHT"
z=txt.swapcase()
print(z)
aa=txt.title()
print(aa)

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))

print(bool(a))
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))