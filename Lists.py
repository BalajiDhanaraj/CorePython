"""
Lists
Lists in Python represent ordered sequences of values. Here is an example of how to create them:
"""

##mutliple list
hands= [
    [2,3,4],
    [3,5,2],
]
#List can contain a mix of different type of variables:

my_favourite_things = [32, 'raindrops on roses', help]


"""Indexing
You can access individual list elements with square brackets.

Which planet is closest to the sun? Python uses zero-based indexing, so the first element has index 0."""

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

print(planets[0])

print(planets[-2])

"""Slicing
What are the first three planets? We can answer this question using slicing:
"""

print(planets[0:3])

"""
planets[0:3] is our way of asking for the elements of planets starting from index 0 and continuing up to but not including index 3.

The starting and ending indices are both optional. If I leave out the start index, it's assumed to be 0. So I could rewrite the expression above as:

"""

print(planets[:3])


"""
If I leave out the end index, it's assumed to be the length of the list.

"""

print(planets[3:])

## we can also use the negative indices when slicing

print(planets[3:-3])


#the last 3 element for the list

print(planets[-3:])

"""
list are mutable meaning they can be modified "in place"
we can modified the list by using index
"""

planets[3] = "sun"

print(planets[0:])


""" List function """

## Find the length of the list by using the function "len"

len(planets)

## sorted the list by using the "sorted" alphabetical order

sorted(planets)

## arithmetic function also can perform by additing list "sum"

primes = [2,4,3,5]

sum(primes)


## MAX AND MIN function also we can perform

min(primes)
max(primes)

## python carry around an assocaited variable called "imag" representing their imaginary part

x= 12
print(x.imag)

c = 12+3j
print(c.imag)
print(x.bit_length())
# help(x.bit_length())


# list methods  -----> append the list

print(planets.append("Earth"))


## remove the element from the list, with pop index ---> last element will be removed from the list

print(planets.pop())

## Searching the list by index

print(planets.index("Earth"))

## using the ""in"" operator to check list have particular elements

print("Earth" in planets)

print("sun" not in planets)

## TUPLES is like a list, but its immutable , we cant change the value or append the value

t = (2,3,5)

print(t[1]) ##index function will work, but not append and no changes

print(len(t))


""" SWAPPING THE TWO VALUES IN PYTHON"""

A = 6
B = 3

A,B = B,A

print(A,B)


"""" Set is collection of data which is unordered, unchangeable
and unindexed, Duplicates is no allowed
"""

myset = {'apple','vanan','cherry'}

print(myset)


diff_data = {11,"apple",True,'a'}
print(diff_data)