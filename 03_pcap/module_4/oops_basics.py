# class - blueprint for creating object
# object - instance of a class. new Car()
# property - variables inside of a class. They describe class's characteristics.
# method - functions inside of a class. They describe actions
# encapsulation - ability of a class to inherit another class
# superclass - parent class from which others inherit
# subclass - child that inherits from a superclass

class Dog:
    def __init__(self, name, breed):
        self.name = name # property
        self.breed = breed # property
        
    def bark(self): # method
        print(f"{self.name} is barking!")
        


buddy = Dog("Buddy", "Golden Retriver")
buddy.bark()

# car class
# properties - brand, model and year
# method - display_info - that will print properties in a nice way
# create 3 different cars