
""" Imports in python """
import math

import numpy as numpy

print("its math! it has type{}".format(type(math)))


print(dir(math))

print("pi to 4 significat digits = {:.5}".format(math.pi))

import math as mt

print(mt.pi)

### numpy function gave us an array

rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)

""" Numpy have the array function """

print(rolls.mean())

## array into a list

print(type(rolls.tolist()))


xlist = [[1,2,3],[2,4,6],]
# Create a 2-dimensional array
x = numpy.asarray(xlist)
print("xlist = {}\nx =\n{}".format(xlist, x))











