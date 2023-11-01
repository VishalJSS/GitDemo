import datetime
#from datetime import timezone,timedelta, datetime

x = datetime.datetime.now()
print(x)                        #2023-10-17 16:34:44.108914
print(x.year)                   #2023
print(x.strftime("%A"))         #Tuesday
print(x.strftime("%a"))         #Tue
print(x.strftime("%B"))         #October
print(x.strftime("%b"))         #Oct
print(x.strftime("%C"))         #20   Century
print(x.strftime("%c"))         #Tue Oct 17 16:34:44 2023
print(x.strftime("%d"))         #17   Day of the month
print(x.strftime("%f"))         #108914  Microsecond
print(x.strftime("%G"))         #2023     ISO 8601 year
print(x.strftime("%H"))         #16     #24 hrs format time
print(x.strftime("%I"))         #24
print(x.strftime("%j"))         #290   Day number of year 001-366
print(x.strftime("%M"))         #34    Minute
print(x.strftime("%m"))         #10    Month
print(x.strftime("%p"))         #PM    AM/PM
print(x.strftime("%S"))         #44    Seconds
print(x.strftime("%U"))         #42    Week number of year, Sunday as the first day of week, 00-53
print(x.strftime("%u"))         #2     ISO 8601 weekday (1-7)
print(x.strftime("%V"))         #42    ISO 8601 weeknumber (01-53)
print(x.strftime("%W"))         #42    Week number of year, Monday as the first day of week, 00-53
print(x.strftime("%w"))         #2     Weekday as a number 0-6, 0 is Sunday
print(x.strftime("%X"))         #16:34:44  Local Version time
print(x.strftime("%x"))         #10/17/23  Local Version Date
print(x.strftime("%Y"))         #2023
print(x.strftime("%y"))         #23
print(x.strftime("%Z"))
print(x.strftime("%z"))
print(x.strftime("%%"))         #%


y = datetime.datetime(2020, 5, 17)
print(y)      #2020-05-17 00:00:00

#dt = datetime(2019, 1, 1, 12, 0, 0, tzinfo=timezone(timedelta(hours=9), 'JST'))
#print(dt.tzname)

import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])   #30

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)      #{"name": "John", "age": 30, "city": "New York"}

print(json.dumps({"name": "John", "age": 30}))    #{"name": "John", "age": 30}
print(json.dumps(["apple", "bananas"]))           #["apple", "bananas"]
print(json.dumps(("apple", "bananas")))           #["apple", "bananas"]
print(json.dumps("hello"))                        #"hello"
print(json.dumps(42))                             #42
print(json.dumps(31.76))                          #31.76
print(json.dumps(True))                           #true
print(json.dumps(False))                          #false
print(json.dumps(None))                           #null

#String formatting
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))    #I want 3 pieces of item number 567 for 49.00 dollars.

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))      #His name is John. John is 36 years old.

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))    #I have a Ford, it is a Mustang.


import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")      #YES! We have a match!
else:
  print("No match")

y = re.findall("ai", txt)
print(y)                    #['ai', 'ai']

z = re.search("\s", txt)
print("The first white-space character is located in position:", z.start())   #The first white-space character is located in position: 3

a = re.split("\s", txt)
print(a)      #['The', 'rain', 'in', 'Spain']

#Split the string at the first white-space character:
b = re.split("\s", txt, 1)
print(b)      #['The', 'rain in Spain']

#Replace all white-space characters with the digit "9":
c = re.sub("\s", "9", txt)
print(c)      #The9rain9in9Spain

#Replace the first two occurrences of a white-space character with the digit 9:
d = re.sub("\s", "9", txt, 2)
print(d)      #The9rain9in Spain

e = re.search("ai", txt)
print(e) #this will print an object   #<re.Match object; span=(5, 7), match='ai'>

#.span() returns a tuple containing the start-, and end positions of the match.
#.string returns the string passed into the function
#.group() returns the part of the string where there was a match

f = re.search(r"\bS\w+", txt)
print(f.span())     #(12, 17)
print(f.string)     #The rain in Spain
print(x.group())    #The rain in Spain

g="I want to learn everything about the regular expression in detail through every site ! in 20 days"
h = re.findall("[a-g]", g)
print(h)    #['a', 'e', 'a', 'e', 'e', 'g', 'a', 'b', 'e', 'e', 'g', 'a', 'e', 'e', 'd', 'e', 'a', 'g', 'e', 'e', 'e', 'd', 'a']
i=re.findall("\d", g)
print(i)    #['2', '0']
j=re.findall("le..n", g)
print(j)    #['learn']
k=re.findall("^every", g)
if x:
  print("Yes, the string starts with 'every'")    #Yes, the string starts with 'every'
else:
  print("No match")

l=re.findall("detail$", g)
if x:
  print("Yes, the string ends with 'detail'")   #Yes, the string ends with 'detail'
else:
  print("No match")

m=re.findall("re.*ar", g)
print(m)      #['regular']

n=re.findall("de.+l", g)
print(n)      #['detail']

o=re.findall("de.?l", g)
p=re.findall("deta.?l",g)
print(o)      #[]
print(p)      #['detail']

q=re.findall("d.{2}s", g)
print(q)      #['days']

txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
print(x)      #['falls']
if x:
  print("Yes, there is at least one match!")      #Yes, there is at least one match!
else:
  print("No match")

r = re.findall("\AThe", txt)
print(r)    #['The']

s = re.findall(r"\bain", txt)  # r is raw text and \b starting with ain
print(s)      #[]

t = re.findall(r"ain\b", txt)  #\b ending with ain
print(t)      #['ain', 'ain', 'ain']

u = re.findall(r"\Bain", txt)   #\B not starting with ain
print(u)      #['ain', 'ain', 'ain', 'ain']

v = re.findall(r"ain\B", txt)   #\B not ending with ain
print(v)      #['ain']

w = re.findall("\d", txt)     #Returns digit 0-9
print(w)      #[]

x = re.findall("\D", txt)   #Return a match at every no-digit character:
print(x)

"""
['T', 'h', 'e', ' ', 'r', 'a', 'i', 'n', ' ', 'i', 'n', ' ', 'S', 'p', 'a', 'i', 'n', ' ', 'f', 'a', 'l', 'l', 's', ' ', 'm', 'a', 'i', 'n', 'l', 'y', ' ', 'i', 'n', ' ', 't', 'h', 'e', ' ', 'p', 'l', 'a', 'i', 'n', '!']
"""

y = re.findall("\s", txt)   #Returns whitespaces
print(y)   #[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

z = re.findall("\S", txt)  #Return a match at every NON white-space character:
print(z)

"""
['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n', 'f', 'a', 'l', 'l', 's', 'm', 'a', 'i', 'n', 'l', 'y', 'i', 'n', 't', 'h', 'e', 'p', 'l', 'a', 'i', 'n', '!']
"""

aa = re.findall("\w", txt)  #Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
print(aa)

"""
['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n', 'f', 'a', 'l', 'l', 's', 'm', 'a', 'i', 'n', 'l', 'y', 'i', 'n', 't', 'h', 'e', 'p', 'l', 'a', 'i', 'n']
"""

bb = re.findall("\W", g)   #Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
print(bb)   #[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '!', ' ', ' ', ' ']

cc = re.findall("Spain\Z", txt)  #Check if the string ends with "Spain":
print(cc)     #[]

dd = re.findall("[ao]", g)
print(dd)     #['a', 'o', 'a', 'a', 'o', 'a', 'o', 'a', 'o', 'a']

ee = re.findall("[^aeiou]", g)
print(ee)

"""
['I', ' ', 'w', 'n', 't', ' ', 't', ' ', 'l', 'r', 'n', ' ', 'v', 'r', 'y', 't', 'h', 'n', 'g', ' ', 'b', 't', ' ', 't', 'h', ' ', 'r', 'g', 'l', 'r', ' ', 'x', 'p', 'r', 's', 's', 'n', ' ', 'n', ' ', 'd', 't', 'l', ' ', 't', 'h', 'r', 'g', 'h', ' ', 'v', 'r', 'y', ' ', 's', 't', ' ', '!', ' ', 'n', ' ', '2', '0', ' ', 'd', 'y', 's']
"""

ff = re.findall("[0-5]", g)
print(ff)     #['2', '0']

gg = re.findall("[01]", g)
print(gg)     #['0']

hh = re.findall("[0-5][0-9]", g)
print(hh)     #['20']

ii = re.findall ("[a-z][A-Z]", g)
jj = re.findall ("[a-z][a-z]", g)
print(ii)   #[]
print(jj)


"""
['wa', 'nt', 'to', 'le', 'ar', 'ev', 'er', 'yt', 'hi', 'ng', 'ab', 'ou', 'th', 're', 'gu', 'la', 'ex', 'pr', 'es', 'si', 'on', 'in', 'de', 'ta', 'il', 'th', 'ro', 'ug', 'ev', 'er', 'si', 'te', 'in', 'da', 'ys']
"""

kk="I know how to use + and - and also i know (person) is {Happy} * | pipline"
ll = re.findall("[+]", kk)
mm = re.findall("[-*.|()${}]", kk)
print(ll)     #['+']
print(mm)     #['-', '(', ')', '{', '}', '*', '|']
