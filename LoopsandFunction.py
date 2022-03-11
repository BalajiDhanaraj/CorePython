
#Loops in python ----> for, rangees

""" Loops is used to repeatedly execute code"""

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # end is used to print in same line

##mutliple using for loops

tables = (1,2,3,4,5,6,7,8,9,10)

for count in range(1,11):
    for tab in tables:
        total = count*tab
        print(count,"*",tab,"=",total)



















