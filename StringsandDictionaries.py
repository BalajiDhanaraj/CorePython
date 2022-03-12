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














