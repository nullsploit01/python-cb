# __name__ - Name of class
# __module__ - MOdue where the class is defined
# __bases__ - Base class of the class
# hasattr() - checks if an object has a specific attribute

class Person:
    def __init__(self, name):
        self.name = name
        
p = Person("Ava")
print(hasattr(p ,"age"))
print(type(p))
print(Person.__name__)
print(Person.__module__)
print(Person.__bases__)