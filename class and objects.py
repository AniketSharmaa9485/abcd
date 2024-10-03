'''class Pets:
    pass
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("hello my name is "+ self.name)

p1 = Pets("John", 30)
p1.myfunc()
'''
#inheritance
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,rname,zname):
        self.popol = rname
        self.oohh = zname
    def func(self):
        print(self.popol,self.oohh)

x = Person("John", "Doe")
x.printname()

