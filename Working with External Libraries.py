
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


""" python file handling 
File Handling
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

"""

f = open(" ","rt")### r == read, t == text

""" Read lInes """
f = open("filename.txt","r")
print(f.readline())


""" write to an existing file """

f = open("demo.txt","a")

f.write("now the file has more content")
f.close()

""" create a new file """

f = open("dem.txt","x") ## x==create a file


"""" Delete a file """

import os
os.remove("demo.txt")

### check if file exist

if os.path.exists("demo.txt"):
    os.remove("demo.txt")
else:
    print("the file does not exist")

""" Delete Folder """

os.rmdir("myfolder")

