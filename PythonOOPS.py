"""   Python class and object
python is the object oriented programmming lanuage

A class is called as blueprint,
A object is called as instance of class
like method and fucntion
"""

##creating class

class Myclass:

    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Myclass("john",33)

print(p1.name,p1.age)

### self is not name self , so we can name what ever we want

class Myclass2:

    def __init__(s1,name="mike",age=55):
        s1.name = name
        s1.age = age
    def myfunc(s2):
        print("hello my name is ",s2.name," ",s2.age)

p2 = Myclass2("walker",22)

p2 = Myclass2()
"""p2.name = "scence"
p2.age = 23
"""
p2.myfunc()


## delete object using  " del "

del p2

## the pass statement ---> class definitions cannot be empty, but if you for some reson have a class
## definition with no content, put in the pass statement to avoid getting an error.

class p1s:
    pass


""" Python Inheritance """


""" Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class. 
"""

## creating a parent class

class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

x = person("hone","doe")

x.printname()

## creating a child class

class student(person):
    pass

## __init__() function

class students(person):

    def __init__(self,fname,lname):
        super().__init__(fname,lname)


x2 = students("mmm","olen")

print(x2.firstname)
print(x2.lastname)



""" python iterators 

iteraotors is an objext that contains a countable number of values

__iter()__

iterator vs iterable

Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator:

"""

mytyple = (34, 43, 234,22)

myiter = iter(mytyple)

print(next(myiter))
print(next(myiter))
print(next(myiter))

for x in myiter:
    print(x)

""" python dates """

import  datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))


""" Python Math """

x = min(3,5,6)
y = max(10,3,6)

print(x)
print(y)

xy = abs(-7.45)

print(xy)

s = pow(4,3)
print(s)

import math

xx = math.sqrt(22)

print(xx)

a = math.ceil(1.4)
b = math.floor(1.4)

print(a)
print(b)














