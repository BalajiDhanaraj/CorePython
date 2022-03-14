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
