x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
for i, j in zip(x, y):
  z.append(i + j)
print(z)        #[5, 7, 9, 11]

import numpy as np
z = np.add(x, y)
print(z)        #[ 5  7  9 11]

print(type(np.add))             #<class 'numpy.ufunc'>
print(type(np.concatenate))     #<class 'numpy._ArrayFunctionDispatcher'>
#The frompyfunc() method takes the following arguments:

#function - the name of the function.
#inputs - the number of input arguments (arrays).
#outputs - the number of output arrays.
#frompyfunc(function,inputs,outputs)

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))        #[6 8 10 12]

if type(np.add) == np.ufunc:
  print('add is ufunc')         #add is ufunc
else:
  print('add is not ufunc')

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr1 = np.add(arr1, arr2)
print(newarr1)      #[30 32 34 36 38 40]

newarr2 = np.subtract(arr1, arr2)
print(newarr2)      #[-10 -10 -10 -10 -10 -10]

newarr3 = np.multiply(arr1, arr2)
print(newarr3)      #[200 231 264 299 336 375]

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

newarr4 = np.divide(arr1, arr2)
print(newarr4)          #[ 3.33333333  4.          3.          5.         25.          1.81818182]

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])
newarr5 = np.power(arr1, arr2)
print(newarr5)      #[      1000    3200000  729000000 -520093696       2500          0]

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr6 = np.mod(arr1, arr2)
print(newarr6)      #[ 1  6  3  0  0 27]

newarr7 = np.remainder(arr1, arr2)
print(newarr7)      #[ 1  6  3  0  0 27]

newarr8 = np.divmod(arr1, arr2)
print(newarr8)      #(array([ 3,  2,  3,  5, 25,  1]), array([ 1,  6,  3,  0,  0, 27]))


arr = np.array([-1, -2, 1, 2, 3, -4])
newarr9 = np.absolute(arr)
print(newarr9)      #[1 2 1 2 3 4]

arr10 = np.trunc([-3.1666, 3.6667])
print(arr10)        #[-3.  3.]

arr11 = np.fix([-3.1666, 3.6667])
print(arr11)        #[-3.  3.]

arr12 = np.around(3.1666, 2)
print(arr12)        #3.17

arr13 = np.floor([-3.1666, 3.6667])
print(arr13)        #[-4.  3.]

arr14 = np.ceil([-3.1666, 3.6667])
print(arr14)        #[-3.  4.]

arr15 = np.arange(1, 10)
print(np.log2(arr15))       #[0.         1.         1.5849625  2.         2.32192809 2.5849625 2.0735492 3.         3.169925  ]

arr16 = np.arange(1, 10)
print(np.log10(arr16))  #[0.         0.30103    0.47712125 0.60205999 0.69897    0.77815125 0.84509804 0.90308999 0.95424251]

arr17 = np.arange(1, 10)
print(np.log(arr17))        #[0.         0.69314718 1.09861229 1.38629436 1.60943791 1.79175947 1.94591015 2.07944154 2.19722458]

from math import log

nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))       #1.7005483074552052

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr18 = np.add(arr1, arr2)
print(newarr18)     #[2 4 6]

newarr19 = np.sum([arr1, arr2])
print(newarr19)     #12

newarr20 = np.sum([arr1, arr2], axis=1)
print(newarr20)     #[6 6]

newarr21 = np.cumsum(arr1)
print(newarr21)     #[1 3 6]

arr21 = np.array([1, 2, 3, 4])
x = np.prod(arr21)
print(x)        #24

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2])
print(x)        #40320

newarr22 = np.prod([arr1, arr2], axis=1)
print(newarr22)     #[  24 1680]

newarr23 = np.cumprod(arr2)
print(newarr23)     #[   5   30  210 1680]

arr24 = np.array([10, 15, 25, 5])
newarr25 = np.diff(arr24)
print(newarr25)     #[  5  10 -20]

newarr26 = np.diff(arr24, n=2)
print(newarr26)     #[  5 -30]

num1 = 4
num2 = 6

x = np.lcm(num1, num2)
print(x)        #12

arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)        #18

arr = np.arange(1, 11)
x = np.lcm.reduce(arr)
print(x)        #2520

num1 = 6
num2 = 9

x = np.gcd(num1, num2)
print(x)        #3

arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)        #4

x = np.sin(np.pi/2)
print(x)        #1.0

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)        #[1.         0.8660254  0.70710678 0.58778525]

arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)        #[1.57079633 3.14159265 4.71238898 6.28318531]

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
print(x)        #[ 90. 180. 270. 360.]

x = np.arcsin(1.0)
print(x)        #1.5707963267948966

arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)        #[ 1.57079633 -1.57079633  0.10016742]

base = 3
perp = 4

x = np.hypot(base, perp)
print(x)        #5.0

#Hyperbolic Functions
x = np.sinh(np.pi/2)
print(x)        #2.3012989023072947

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr)
print(x)            #[2.50917848 1.60028686 1.32460909 1.20397209]

#Angles
x = np.arcsinh(1.0)
print(x)        #0.881373587019543

#Angles
arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
print(x)        #[0.10033535 0.20273255 0.54930614]

#Sets
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)        #[1 2 3 4 5 6 7]

#Union
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)
print(newarr)       #[1 2 3 4 5 6]

#Intersection
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print(newarr)       #[3 4]

#Difference
newarr = np.setdiff1d(arr1, arr2, assume_unique=True)
print(newarr)       #[1 2]

#Symmetric Difference
newarr = np.setxor1d(arr1, arr2, assume_unique=True)
print(newarr)       #[1 2 5 6]
import pdb;pdb.set_trace()