"""This is comment section"""
a=1
b="One"
c=2.0
print(type(a), type(b), type(c))
print("Hello World")
d,e,f="two","three","four"
g=h=i=3
print(d,e,f,g,h,i)
print("Additon of Numbers", a+g)
print("String add", b+d)
j=["five",4,5.0]
k=("six",6)
l=range(5)
print("list", j[0],j[-1])
print("tuple", k[-2])
for m in l:
    print(m)
n=print(len(l))
o="I am doing Good"
print("Good" in o)
if "Nothing" not in o:
    print("Nothing is not in {}".format(o))