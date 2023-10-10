a=1
b=2
c=3
d=4
e=5

f=a+b
g=e-a
h=c*d
i=e/c
j=e%c
k=e//c
l=b**c

print("Add", f, "\nSub", g, "\nmul", h, "\ndiv", i, "\nmod", j, "\nfloor", k, "\nexpo", l )

m=c<<2   #   8421   0011  3  1100   12
print(m)
n=c>>2   #   0011   3    0000   0
print(n)

# &, |, ^

o=3 & 2  # 0011  &  0010    = 0010  2
p=3 | 2  # 0011  |  0010    = 0011  3
q=3 ^ 2  # 0011  ^  0010    = 0001  1     Sets each bit to 1 if only one of two bits is 1
r=~o     #  ~0010  = 1101
print(o)
print(p)
print(q)
print(r)

#()	Parentheses
#**	Exponentiation
#+x  -x  ~x	Unary plus, unary minus, and bitwise NOT
#*  /  //  %	Multiplication, division, floor division, and modulus
#+  -	Addition and subtraction
#<<  >>	Bitwise left and right shifts
#&	Bitwise AND
#^	Bitwise XOR
#|	Bitwise OR
#==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators
#not	Logical NOT
#and	AND
#or	OR