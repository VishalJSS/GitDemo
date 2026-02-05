import numpy as np
x=10

#Method 1
if x>0:
    print(x, " is positve")
elif x<0:
    print(x, " is negative")
else:
    print(x, " is zero")

#Method 2:
y = -10
input_sign=np.sign(y)

if input_sign ==1:
    print(y, "is a positive number")
elif input_sign ==-1:
    print(y, " is a negative number")
else:
    print(y, " is zero")