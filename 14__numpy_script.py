import numpy as np
import time
import sys

print("\nSection 1")
#1D Array
start = time.time()
listnom = [1,2, 3, 4, 5]
arr = np.array([1, 2, 3, 4, 5])
print(arr)              #[1 2 3 4 5]
print(type(arr))        #<class 'numpy.ndarray'>
print(np.__version__)   #1.26.1
print(arr.ndim)         #1
print("Time take for the above execution :", time.time() - start)   #Consumes less time
print("Listsize", sys.getsizeof(listnom) )  # Big space consumed by list
print("Arraysize", arr.nbytes)              # Less space consummed by array

print("\nSection 2")
#Tuple array
arr1 = np.array((1,2,3,4,5))
print(arr1)         #[1 2 3 4 5]
arrcreatecount = np.linspace(0,10,5)    #Create 5 values between 0 and 1
print(arrcreatecount)
arrrange = np.arange(0,10, 2)
print(arrrange)
arrlogspace = np.logspace(1,3,4)    #shows values of 10^1 to 10^3 with 4 values
print(arrlogspace)

print("\nSection 3")
#0D Array
arr2 = np.array(42)
print(arr2)         #42
print(arr2.ndim)    #0

#zeros
arr0 = np.zeros(5)
print(arr0)
arr02d = np.zeros([2,3])
print(arr02d)

#ones
arr1ones = np.ones(5, dtype=int)    #Create 5 1 dimensinal data with only 1
print(arr1ones)
arr1one2d = np.ones([4,2])  #Without dtype
print(arr1one2d)

#full(desired number in array)
arrdesir =  np.full(10,3)
print(arrdesir)
arrdesidim = np.full([3,4], 9)
print(arrdesidim)

print("\nSection 4")
#2D Array
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr3)             #[[1 2 3]   [4 5 6]]
print(arr3.ndim)        #2

#3D Array
arr4 = np.array([ [[1, 2, 3], [4, 5, 6]],
                  [[1, 2, 3], [4, 5, 6]] ])
print(arr4)                     # [[1 2 3]  [4 5 6]]]
print(arr4.ndim)                #3
print(arr4.shape)               #Dimensional shape

#Higher Dimension Creation

arr5 = np.array([1, 2, 3, 4], ndmin=5)
print(arr5)                             #[[[[[1 2 3 4]]]]]
print('number of dimensions :', arr5.ndim)   #number of dimensions : 5

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#Getting array elements
print(arr[0])               #1

print("\nSection 5")
#Adding
print(arr[2]+arr[3])           #3+4 = 7

#Slicing
print(arr[1:5])     #[2 3 4 5]
print(arr[4:])      #[ 5  6  7  8  9 10]
print(arr[-3:-1])   #[8 9]
print(arr[1:5:2])   #[2 4]
print(arr[ : :-1])  #

#Getting in 2D array
arr6 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr6[0, 1])    #2
#Negative Indexing
print('Last element from 2nd dim: ', arr6[1, -1])  #10
#Slicing
print(arr6[1, 1:4])   #[7 8 9]
print(arr6[0:2, 2])   #[3 8]
print(arr6[0:2, 1:4])  #[[2 3 4] [7 8 9]]

print("\nSection 6")
#Access 3D Array
arr7 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr7[0, 1, 2])      #6

"""datatypes
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
    """

arr8 = np.array(['apple', 'banana', 'cherry'])
print(arr8.dtype)    #<U6

arr9 = np.array([1, 2, 3, 4], dtype='S')
print(arr9)    #[b'1' b'2' b'3' b'4']
print(arr9.dtype)  #|S1

#Size specification
arr10 = np.array([1, 2, 3, 4], dtype='i4')
print(arr10)
print(arr10.dtype)

#A non integer string like 'a' can not be converted to integer (will raise an error):
#arr = np.array(['a', '2', '3'], dtype='i')

print("\nSection 7")

arr11 = np.array([1.1, 2.1, 3.1])
print(arr11.dtype)      #float64
newarr = arr11.astype('i')  #other way -  newarr = arr11.astype(int)
print(newarr)       #[1 2 3]
print(newarr.dtype) #int32
strarr = arr11.astype(np.int64)
print(strarr)
print(strarr.dtype)
print(arr11.size)
#typecasting = np.array['1', '1.25', 'string']
#errortypecast = typecasting.astype(np.int64)
#print(errortypecast)

#Make a copy, change the original array, and display both arrays:
arr12 = np.array([1, 2, 3, 4, 5])
x = arr12.copy()
arr12[0] = 42
print(arr12)            #[42  2  3  4  5]
print(x)                #[1 2 3 4 5]

print("\nSection 8")
#Make a view, change the original array, and display both arrays:
arr13 = np.array([1, 2, 3, 4, 5])
y = arr13.view()
arr13[0] = 42
print(arr13)            #[42  2  3  4  5]
print(y)                #[42  2  3  4  5]

#Every NumPy array has the attribute base that returns None if the array owns the data.
#Otherwise, the base  attribute refers to the original object.
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)           #None
print(y.base)           #[1 2 3 4 5]

print('shape of array :', arr5.shape)       #shape of array : (1, 1, 1, 1, 4)

arr14 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr14.reshape(4, 3)
print(newarr)           #[[ 1  2  3]  [ 4  5  6]  [ 7  8  9]  [10 11 12]]

arr15 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr15.reshape(2, 3, 2)
print(newarr)
"""[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]]
"""

print("\nSection 9")
#Unknown dimension
arr16 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr16.reshape(2, 2, -1)
print(newarr)
'''
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
'''
#Flattening
arr17 = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr17.reshape(-1)
print(newarr)      #[1 2 3 4 5 6]

arr18 = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr18:
  print(x)
'''  
[1 2 3]
[4 5 6]
'''
for x in arr18:
  for y in x:
    print(y)    #1 2 3 4 5 6

print("\nSection 10")
arr19 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr19:
  for y in x:
    for z in y:
      print(z)  #1 2 3 4 5 6 7 8 9 10 11 12

for x in np.nditer(arr19):
  print(x)              # 1 2 3 4 5 6 7 8 9 10 11 12

#Itering with diff data type
arr20 = np.array([1, 2, 3])
for x in np.nditer(arr20, flags=['buffered'], op_dtypes=['S']):
  print(x)  #b'1'  b'2' b'3'
for idx, x in np.ndenumerate(arr20):
  print(idx, x)     #(0,) 1 (1,) 2 (2,) 3

print("\nSection 11")
#Iterating on each scalar element
arr21 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr21[:, ::2]):
  print(x)      # 1 3 5 7
for idx, x in np.ndenumerate(arr21):
  print(idx, x)

"""
(0, 0) 1
(0, 1) 2
(0, 2) 3
(0, 3) 4
(1, 0) 5
(1, 1) 6
(1, 2) 7
(1, 3) 8
"""

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)   #[1 2 3 4 5 6]

arr = np.stack((arr1, arr2), axis=1)
print(arr)     #Stack
"""
[[1 4]
 [2 5]
 [3 6]]
"""

print("\nSection 12")

arr = np.hstack((arr1, arr2))
print(arr)     #Along rows  [1 2 3 4 5 6]

arr = np.vstack((arr1, arr2))
print(arr)    #Along Columns
"""
[[1 2 3]
 [4 5 6]]
"""

arr = np.dstack((arr1, arr2))
print(arr)    #Along Height/depth

"""
[[[1 4]
  [2 5]
  [3 6]]]
"""

print("\nSection 13")
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)   #[[1 2 5 6] [3 4 7 8]]

arr22 = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr22, 3)
print(newarr)  #[array([1, 2]), array([3, 4]), array([5, 6])]

print("\nSection 14")
arr23 = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr23, 4)
print(newarr)   #[array([1, 2]), array([3, 4]), array([5]), array([6])]


arr24 = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr24, 3)
print(newarr[0])   #[1 2]
print(newarr[1])   #[3 4]
print(newarr[2])   #[5 6]

arr25 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr25, 3, axis=1)
print(newarr)

"""
[array([[ 1],
       [ 4],
       [ 7],
       [10],
       [13],
       [16]]), array([[ 2],
       [ 5],
       [ 8],
       [11],
       [14],
       [17]]), array([[ 3],
       [ 6],
       [ 9],
       [12],
       [15],
       [18]])]
"""

print("\nSection 15")
arr26 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr26, 3)
print(newarr)

"""
[array([[ 1],
       [ 4],
       [ 7],
       [10],
       [13],
       [16]]), array([[ 2],
       [ 5],
       [ 8],
       [11],
       [14],
       [17]]), array([[ 3],
       [ 6],
       [ 9],
       [12],
       [15],
       [18]])]
"""
newarr1 = np.vsplit(arr26, 3)
print(newarr1)
"""
[array([[1, 2, 3],
       [4, 5, 6]]), array([[ 7,  8,  9],
       [10, 11, 12]]), array([[13, 14, 15],
       [16, 17, 18]])]
"""

print("\nSection 16")

arr27 = np.array([1, 2, 3, 4, 5, 4, 4, 6, 7, 8, 9])
x = np.where(arr27 == 4)
print(x)     # (array([3, 5, 6], dtype=int64),)
y = np.where(arr27%2 == 0)    #Even
print(y)     #(array([1, 3, 5, 6, 7, 9], dtype=int64),)
z = np.where(arr27%2 == 1)    #Odd
print(z)  #(array([ 0,  2,  4,  8, 10], dtype=int64),)

a = np.searchsorted(arr27, 7)
print(a)  #8
b = np.searchsorted(arr27, 7, side='right')
print(b)   #9

arr28 = np.array([1, 3, 5, 7])
c = np.searchsorted(arr28, [2, 4, 6])  #Search for insertion index
print(c)     #[1 2 3]

print("\nSection 17")

arr29 = np.array([3, 2, 0, 1])
print(np.sort(arr29))  #[0 1 2 3]

arr30 = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr30))  #['apple' 'banana' 'cherry']

arr31 = np.array([True, False, True])
print(np.sort(arr31))  #[False  True  True]

arr32 = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr32))  # [[2 3 4]  [0 1 5]]

print("\nSection 18")
arr33 = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr33[x]
print(newarr)   #[41 43]

arr34 = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []
#empty array (unintialized)
emparr = np.empty
print(emparr)
empdimarr = np.empty([2,2])
print(empdimarr)
print("\nSection 19")
# go through each element in arr
for element in arr34:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr34[filter_arr]

print(filter_arr)    #[False, False, True, True]
print(newarr)      #[43 44]

arr33 = np.array([41, 42, 43, 44])
filter_arr = arr33 > 42
newarr = arr33[filter_arr]
print(filter_arr)   #[False False  True  True]
print(newarr)     #[43 44]

print("\nSection 20")
#random
arr34 = np.random.rand(10)    #give random value between 0 and 1 (10 values)
print(arr34)
arr35 = np.random.rand(4,5)   #Equally space random values floating
print(arr35)
arr36 = np.random.randn(2,3)   #random number with 0 as center Equally distributed
print(arr36)
arr37 = np.random.randint(10,100)   #By default returns 1 value if not provided size
print(arr37)
arr38 = np.random.randint(10,100, size=(2,3))
print(arr38)

#datatype
arr39 = np.array([1,2,3.1,4,5])   #Even 1 value is float, it will consider all as float value
print(arr39)    #[1.  2.  3.1 4.  5. ]
listvalue = [1, 'string', 5.6, 1000]
arr40 = np.array(listvalue)     #all values in list will be considered string
print(arr40)  #['1' 'string' '5.6' '1000']
                 