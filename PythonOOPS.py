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

##





