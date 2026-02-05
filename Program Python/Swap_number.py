a = 10
b = 20

#Method 1 (Without temp)
a,b = b, a

print("a value is ", a)
print("b value is ", b)

c = 30
d = 40
#Method 2 (with temp variable)

temp = c
c = d
d = temp

print("c value after temp", c)
print("d value after temp", d)

#Method 3 (with arithmetic operation)

e = 50
f = 60

e=e+f  #Summation 110
f=e-f  #getting sub value 110-60
e=e-f  #getting other value 110-50

print("e after operation ", e)
print("f after operation ", f)
