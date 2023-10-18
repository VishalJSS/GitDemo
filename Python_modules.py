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
print(y)

#dt = datetime(2019, 1, 1, 12, 0, 0, tzinfo=timezone(timedelta(hours=9), 'JST'))
#print(dt.tzname)

import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#String formatting
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))


import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

y = re.findall("ai", txt)
print(y)

z = re.search("\s", txt)
print("The first white-space character is located in position:", z.start())

a = re.split("\s", txt)
print(a)

#Split the string at the first white-space character:
b = re.split("\s", txt, 1)
print(b)

#Replace all white-space characters with the digit "9":
c = re.sub("\s", "9", txt)
print(c)

#Replace the first two occurrences of a white-space character with the digit 9:
d = re.sub("\s", "9", txt, 2)
print(d)

e = re.search("ai", txt)
print(e) #this will print an object

#.span() returns a tuple containing the start-, and end positions of the match.
#.string returns the string passed into the function
#.group() returns the part of the string where there was a match

f = re.search(r"\bS\w+", txt)
print(f.span())
print(f.string)
print(x.group())

g="I want to learn everything about the regular expression in detail through every site ! in 20 days"
h = re.findall("[a-g]", g)
print(h)
i=re.findall("\d", g)
print(i)
j=re.findall("le..n", g)
print(j)
k=re.findall("^every", g)
if x:
  print("Yes, the string starts with 'every'")
else:
  print("No match")

l=re.findall("detail$", g)
if x:
  print("Yes, the string ends with 'detail'")
else:
  print("No match")

m=re.findall("re.*ar", g)
print(m)

n=re.findall("de.+l", g)
print(n)

o=re.findall("de.?l", g)
p=re.findall("deta.?l",g)
print(o)
print(p)

q=re.findall("d.{2}s", g)
print(q)

txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

r = re.findall("\AThe", txt)
print(r)

s = re.findall(r"\bain", txt)  # r is raw text and \b starting with ain
print(s)

t = re.findall(r"ain\b", txt)  #\b ending with ain
print(t)

u = re.findall(r"\Bain", txt)   #\B not starting with ain
print(u)

v = re.findall(r"ain\B", txt)   #\B not ending with ain
print(v)

w = re.findall("\d", txt)     #Returns digit 0-9
print(w)

x = re.findall("\D", txt)   #Return a match at every no-digit character:
print(x)

y = re.findall("\s", txt)   #Returns whitespaces
print(y)

z = re.findall("\S", txt)  #Return a match at every NON white-space character:
print(z)

aa = re.findall("\w", txt)  #Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
print(aa)

bb = re.findall("\W", g)   #Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
print(bb)

cc = re.findall("Spain\Z", txt)  #Check if the string ends with "Spain":
print(cc)

dd = re.findall("[ao]", g)
print(dd)

ee = re.findall("[^aeiou]", g)
print(ee)

ff = re.findall("[0-5]", g)
print(ff)

gg = re.findall("[01]", g)
print(gg)

hh = re.findall("[0-5][0-9]", g)
print(hh)

ii = re.findall ("[a-z][A-Z]", g)
jj = re.findall ("[a-z][a-z]", g)
print(ii)
print(jj)

kk="I know how to use + and - and also i know (person) is {Happy} * | pipline"
ll = re.findall("[+]", kk)
mm = re.findall("[-*.|()${}]", kk)
print(ll)
print(mm)
