

#Basic function of pythong

user_input = str(input("enter the user name:"))

print("hello world",user_input)

# Numbers and arithmetic in Python

spam_amount=5

print(type(spam_amount)) ##int

print(type(13.23)) ##float

"""##Operator	Name	Description
a + b	Addition	Sum of a and b
a - b	Subtraction	Difference of a and b
a * b	Multiplication	Product of a and b
a / b	True division	Quotient of a and b
a // b	Floor division	Quotient of a and b, removing fractional parts
a % b	Modulus	Integer remainder after division of a by b
a ** b	Exponentiation	a raised to the power of b
-a	Negation	The negative of a"""

## Addtion of two number

a = 10
b = 5
c = 2
print("Addition",a+b)

print("Sub",a-b)

print("true divison",a/b)

print("floor division",a//c)

#order of operation ---> PEMDAS --> Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.

print(8-3+2)
print(-3+4*2)

#example

hat_height_cm = 25
my_height_cm = 190
# How tall am I, in meters, when wearing my hat?
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =", total_height_meters, "?")

total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters =", total_height_meters)

"""#Builtin functions for working with numbers
min and max return the minimum and maximum of their arguments, respectively...
"""
print(min(3,2,9))
print(max(1,0,24))

#abs returns the absolute value of an argument:

print(abs(23.9))
print(abs(-34))

