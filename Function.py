
# Defining Function


def least_difference(a ,b ,c):
    diff1 = abs( a -b)
    diff2 = abs( b -c)
    diff3 = abs( a -c)
    return min(diff1 ,diff2 ,diff3)

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7)
)


# function with default argument

def greet(who="walker"):
    print("hello" ,who)

greet()
greet(who="man")
greet("python")


def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n', # '\n' is the newline character - it starts a new line
)

#Booleans and Conditonals

x=True
y=False
print(type(x),type(y))

"""Comparison Operations
Operation	Description		Operation	Description
a == b	a equal to b		a != b	a not equal to b
a < b	a less than b		a > b	a greater than b
a <= b	a less than or equal to b		a >= b	a greater than or equal to b
"""
def comp(a,b):

    x=a
    y=b
    greaterequal = x>=b
    lessequal = x<=b
    equal= x==y
    notequl = x!=b

    return greaterequal,lessequal,equal,notequl


print("a is greater than eqaul b",comp(10,11))

"""Combining Boolean Values
You can combine boolean values using the standard concepts of "and", "or", and "not". In fact, the words to do this are: and, or, and not.
"""

def primeelection(age, indian_citizen ):
    return (age>=45) and indian_citizen

def primeelection(age, indian_citizen ):
    return (age>=45) or indian_citizen

def primeelection(age, indian_citizen ):
    return (age>=45) or not indian_citizen

print("indian citizen",primeelection(46,True))
print("Isn't Indian citizen",primeelection(45,False))
print("Indian citizen",primeelection(30,False))

def checkweather(have_umbrella,rain_level,have_hood,is_workday):
    prepared_for_weather = (
            have_umbrella
            or ((rain_level < 5) and have_hood)
            or (not (rain_level > 0 and is_workday))
    )
    return prepared_for_weather

print("Is good to go out :",checkweather(False,0,True,True))


"""Conditionals
Booleans are most useful when combined with conditional statements, using the keywords if, elif, and else.

Conditional statements, often referred to as if-then statements, let you control what pieces of code are run based on the value of some Boolean condition. Here's an example:"""

def grade(x):
    if x>=85:
        print("A grade",x)
    elif x>=60 or x>=75:
        print("B grade",x)
    elif x>=35 or x>=55:
        print("c grade",x)
    else:
        print("Keep try again to score! good work",x)

grade(-36)

"""Lambda function"""


x = lambda a : a+10

print(x(5))

## why we using the lambda function, its a anonymous function inside another function

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(10)

print(mydoubler(5))










































