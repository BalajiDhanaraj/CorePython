
#Loops in python ----> for, rangees

"""
for(int i=0;i<2;i++){
    if
}

"""

""" Loops is used to repeatedly execute code"""
print("\n")

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # end is used to print in same line

print("\n")

##mutliple using for loops

tables = (1,2,3,4,5,6,7,8,9,10)

# for count in range(1,11):
#     for tab in tables:
#         total = count*tab
#         print(count,"*",tab,"=",total)

"""Loop through each character in a string"""

s="steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video."

for char in s:
    if char.isupper():
        print(char,end=" ")

print("\n")

""" Range in for loops
range() is a function that returns a sequence of numbers,
"""

for i in range(5):
    print("Doing important work in ",i)


print("\n")

"""While loops ----> 
the while loop is also like for loop but, it have condition to check if the ranges of the while loops
"""

i = 0
while i<10:
    print(i,end="")
    i+=1

print("\n")

for j in range(0,10):
    if j<5:
        print("inner if",j)

print("outer loops \n",j)

"""List comprehensions"""

squares = [n**2 for n in range(10)]

print(squares)
"""---another way to do the list comprehension---"""
sq = []

for __n in range(10):
    sq.append(__n**2)

print(sq)

print("\n")

"""" use the if condition in the list comprehension"""

short_planet= [pl## we in list , pl variable is use to append the value in the list
               for pl in planets ## planets have the list of data like ---"earth,venus"
               if len(pl)<6
               ] ## if condition is to check the


print(short_planet)

print("\n")

sp =[]

for sp in planets:
    if len(sp)<8:
        print(sp)
print(sp)








