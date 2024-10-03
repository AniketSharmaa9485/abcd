'''class abc:
    def __init__(obj1,ro,mo):
        obj1.ro = ro
        obj1.mo = mo
    def execute(obj1):
        print("Good")

class xyz:
    def __init__(obj2,ho,lo):
        obj2.ho = ho
        obj2.ho = ho

    def execute(obj2):
        print("Better")

class mno:
    def __init__(obj3,ko,jo):
        obj3.ko = ko
        obj3.jo = jo

    def execute(obj3):
        print("perfect")

obj1 = abc("roona","mona")
obj2 = xyz("home","lome")
obj3 = mno("komo","jojo")
for x in (abc,xyz,mno):
    x.execute(obj1)

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Inherited from Animal class
dog.bark()   # Defined in Dog class

class Father:
    def work(self):
        print("Father works")

class Mother:
    def cook(self):
        print("Mother cooks")

class Child(Father, Mother):  # Child inherits from both Father and Mother
    def play(self):
        print("Child plays")

child = Child()
child.work()  # Inherited from Father
child.cook()  # Inherited from Mother
child.play()  # Defined in Child

class Animal:
    def eat(self):
        print("Animal eats")

class Mammal(Animal):  # Mammal inherits from Animal
    def walk(self):
        print("Mammal walks")

class Dog(Mammal):  # Dog inherits from Mammal
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.eat()   # Inherited from Animal
dog.walk()  # Inherited from Mammal
dog.bark()  # Defined in Dog

class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

class Cat(Animal):  # Cat inherits from Animal
    def meow(self):
        print("Cat meows")

dog = Dog()
cat = Cat()

dog.eat()  # Inherited from Animal
dog.bark()  # Defined in Dog

cat.eat()  # Inherited from Animal
cat.meow()  # Defined in Cat
'''
class Animal:
    def eat(self):
        print("Animal eats")

class Mammal(Animal):  # Single Inheritance (Mammal -> Animal)
    def walk(self):
        print("Mammal walks")

class Bird(Animal):  # Single Inheritance (Bird -> Animal)
    def fly(self):
        print("Bird flies")

class Bat(Mammal, Bird):  # Multiple Inheritance (Bat -> Mammal and Bird)
    def night_fly(self):
        print("Bat flies at night")

bat = Bat()
bat.eat()     # Inherited from Animal
bat.walk()    # Inherited from Mammal
bat.fly()     # Inherited from Bird
bat.night_fly()  # Defined in Bat
