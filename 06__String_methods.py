r="This can be rough multiple times"
print(r.capitalize())       #This can be rough multiple times
print(r.casefold())         #this can be rough multiple times
print(r.center(80))         #                        This can be rough multiple times
print(r.count('t'), r.count('e'))       # 2 3
print(r.encode())           #b'This can be rough multiple times'
print(r.endswith('s'))      #True
print(r.startswith('T'))    #True
print(r.expandtabs(20))     #This can be rough multiple times
print(r.find('e'))          #10
s={"t":"something", "u":"Nothing"}
print('{t}{u}'.format_map(s))       #somethingNothing
print(r.index('b'))         #9
v=["Victory", "32573", "@#$", "treat", 128, "4.0", 6, " space"]
print(v[0].isalpha())       #True
print(v[5].isdecimal())     #False
print(v[1].isdigit())       #True
print(v[3].isdigit())       #False
print(v[1].isnumeric())     #True
print(v[3].islower())       #True
print(v[3].isupper())       #False
#print(v[4].isascii())
#A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
print(v[0].isidentifier())      #True
print(v[7][0].isspace())        #True
w="This is to check\n"
print(w.isprintable())          #False
print(w.istitle())              #False
print(v[0].istitle())           #True
print(w.join(s))                #tThis is to check      u
print(r.ljust(60,"0"))      #This can be rough multiple times0000000000000000000000000000
print(r.rjust(60,"0"))      #0000000000000000000000000000This can be rough multiple times
x="      Testing     "
print(x.lstrip())
print(x.rstrip())
"""
Testing     
      Testing
"""

y = ",,,,,ssaaww.....banana"
print(y.lstrip(",.asw"))
mytable=str.maketrans("T","B")
print(x.translate(mytable))

"""
banana
      Besting 
"""

txt = "Good night Sam!"
x = "Sam"
y = "Joe"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(mytable)    #Ascii code number is shown with relevant replacement numbers #{83: 74, 97: 111, 109: 101, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mytable))       #G i Joe!

x="abcdefghijklmnopqrstuvwxyz"
y="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mytable=str.maketrans(x,y)
print(mytable)

"""
{97: 65, 98: 66, 99: 67, 100: 68, 101: 69, 102: 70, 103: 71, 104: 72, 105: 73, 106: 74, 107: 75, 108: 76, 109: 77, 110: 78, 111: 79, 112: 80, 113: 81, 114: 82, 115: 83, 116: 84, 117: 85, 118: 86, 119: 87, 120: 88, 121: 89, 122: 90}
"""
print(txt.partition("night"))       #('Good ', 'night', ' Sam!')
print(txt.partition("midnight"))        #('Good night Sam!', '', '')

#Replace
pat = "one one was a race horse, two two was one too."
x = pat.replace("one", "three", 2)
print(x)        #three three was a race horse, two two was one too.

#Index of element last occurence
z="It is too late to obey the orders now"
element=z.rfind("o")
print (element)     #35
limit=z.rfind("o", 1, 12)
print(limit)        #8
change=z.rindex("o", 1, 12)
print(change)       #8

#string.rsplit(separator, maxsplit)

lis="Apple, Banana, Cherry"
li=lis.rsplit( ',')
print(li)       #['Apple', ' Banana', ' Cherry']
maxsplit=lis.rsplit(',', 1)
print(maxsplit)     #['Apple, Banana', ' Cherry']

txt="Welcome to the Jungle of India"
res=txt.split()
print(res)      #['Welcome', 'to', 'the', 'Jungle', 'of', 'India']
lim=txt.split(" ", 3)
print(lim)      #['Welcome', 'to', 'the', 'Jungle of India']
txt="hello,i,am,paul"
fin=txt.split(",")
print(fin)      #['hello', 'i', 'am', 'paul']

#splitlines
txt="I am very Happy\nProud of your achievements"
first=txt.splitlines()
print(first)        #['I am very Happy', 'Proud of your achievements']
second=txt.splitlines(True)
print(second)       #['I am very Happy\n', 'Proud of your achievements']

txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
y = txt.startswith("Hel")
print(x)        #True
print(y)        #True

txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)        #banana

txt="i AM RIGHT"
z=txt.swapcase()
print(z)        #I am right
aa=txt.title()
print(aa)       #I Am Right

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))      #00000hello
print(b.zfill(10))      #welcome to the jungle
print(c.zfill(10))      #000010.000

print(bool(a))      #True
print(bool(False))      #False
print(bool(None))       #False
print(bool(0))          #False
print(bool(""))         #False
print(bool(()))         #False
print(bool([]))         #False
print(bool({}))         #False