from numpy import random
import numpy as np

a = random.randint(100)
print(a)            #55

b = random.rand()
print(b)            #0.9187064171532797

bb = random.rand(5)
print(bb)           #[0.00096148 0.80426094 0.26967834 0.81537053 0.42728369]

c=random.randint(100, size=(5))
print(c)            #[20 12 35 97  2]

d = random.randint(100, size=(3, 5))
print(d)
"""
[[ 6 71 13  8 65]
 [ 8 87 52 87 19]
 [65  5 66 17 81]]
"""

#A random distribution is a set of random numbers that follow a certain probability density function.
e = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(e)
"""
[7 3 7 7 5 7 3 5 7 7 7 5 7 7 7 7 5 3 7 5 5 7 7 5 7 7 7 7 3 5 3 5 3 7 7 7 7
 7 7 7 5 7 7 7 5 7 5 7 5 5 7 5 3 5 7 7 7 5 7 7 5 7 7 7 7 5 7 5 7 7 7 7 7 7
 5 7 7 7 3 7 3 7 7 3 7 7 5 7 7 7 7 7 7 5 3 7 7 5 5 7]
"""

f = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(f)
"""
[[7 5 5 7 7]
 [3 7 7 5 7]
 [5 3 7 7 5]]
"""

g = np.array([1, 2, 3, 4, 5])
random.shuffle(g)
print(g)            #[3 2 5 4 1]
h = np.array([1, 2, 3, 4, 5])
print(random.permutation(h))        #[1 5 4 3 2]