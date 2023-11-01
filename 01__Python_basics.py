"""This is comment section"""
a=1
b="One"
c=2.0
print(type(a), type(b), type(c))    #<class 'int'> <class 'str'> <class 'float'>
print("Hello World")                #Hello World
d,e,f="two","three","four"
g=h=i=3
print(d,e,f,g,h,i)                  #two three four 3 3 3
print("Additon of Numbers", a+g)    #Additon of Numbers 4
print("String add", b+d)            #String add Onetwo
j=["five",4,5.0]
k=("six",6)
l=range(5)
print("list", j[0],j[-1])           #list five 5.0
print("tuple", k[-2])               #tuple six
for m in l:
    print(m)                        #0 1 2 3 4
n=print(len(l))                     #5
o="I am doing Good"
print("Good" in o)                  #True
if "Nothing" not in o:
    print("Nothing is not in {}".format(o))  #Nothing is not in I am doing Good