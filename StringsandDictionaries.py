"""Strings and Dictionaries
Working with strings and dictionaries, two fundamental Python data types"""

##String syntax

x = 'Pluto si a planet'
y = "Pluto is a planet"

print("Pluto\"s  is a planet")

"""The table below summarizes some important uses of the backslash character.

What you type...	What you get	example	print(example)
\'	'	'What\'s up?'	What's up?
\"	"	"That's \"cool\""	That's "cool"
\\	\	"Look, a mountain: /\\"	Look, a mountain: /\
\n	
"1\n  2 3" 1 2 3
"""

print("That's \"cool\" ")

print("That is \ncooler")

print("hello cool",end=" ")
print("cool")
print("cool")


"""Strings are sequences"""

planet = "pluto"

print(planet[2])

print(planet[:-1])
# slicing
print(planet[-3:])
print(len(planet))

print([char+'!' for char in planet])

"""" string does not support the modify them """
# planet[0]='b'
# print(planet)

""" String Methods """

course = "python is a programming"

print(course.upper())

print(course.lower())

print(course.index("th"))

print(course.startswith("py"))

print(course.endswith("on"))

""" Strings and list have function ----> .split() and .join()"""

date = '1955-01-31'
year, month, day = date.split('-')
print(year,month,day)

print('/'.join([month,day,year]))

print('🐍'.join([world.upper() for world in course ]))

""" string format using + operator """

position = 9
print(planet+" you\' always be the "+ str(position)+" the planet to me")

""" another way to using the format {}"""

print("{},you'll always be the {}th planet to me".format(planet,position))


pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390

print("{} weighs about{:.2} kilograms ({:.3%} of earth's mass). Its is home to {:,} Plutonians.".format(
    planet,pluto_mass,pluto_mass/earth_mass,population
))

"""format using index """

s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)

d = "Pluto's a{0} \n"\
    "\n No, it's a {1}." \
    "\n {0}! " \
    "\n {1}! ".format('planet','dwarf planet')

print(d)

""" Dictionaries """

number = {'one':1,'two':2,'three':3}

print(number['one'])


""" in Dictionaries we can able to add the new data with key or value both way can add or changes"""

number['eleven'] = 11
print(number)

""" dictionary also have the comprehension with same syntax similar to the list"""

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planet_to_initial ={planet:planet[0]
                    for planet in planets}

print(planet_to_initial,sep='')

""" in operator """
print('Saturn' in planet_to_initial)

""" a for loop over a dictionary will loop over ist keys """

for k in number:
    print("{}={}".format(k,number[k]))

""" sorting dic """

print(sorted(planet_to_initial))
print('-'.join(sorted(planet_to_initial)))

"""" the very useful \n dict.items \n  methods lets us iterate over the 
keys and values
"""
### rjust is attribute for right side, ljust is attribute for left side
for planeti, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planeti.ljust(20),initial))





