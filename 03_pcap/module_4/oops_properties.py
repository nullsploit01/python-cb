# instance variables - unique to each object
# class variables - shared across all the objects

class Student:
    school_name = "ABC School" # Class variable
    
    def __init__(self, name):
        self.name = name # instance variable
        self.__id = 1234 # private variable
        
alice = Student("Alice")
print(alice.name)
print(alice.school_name)
print(alice._Student__id) # accesing a private variable

print(alice.__dict__)

# create a library class 
# class variable - library_name
# instance variable - book_title and author
# private variable - copies

class Calculator:
    def __init__(self, number, number2):
        self.number = number
        self.number2 = number2
        
    def square(self):
        return self.number ** 2
    
    def exponent(self):
        return self.number ** self.number2
    
c = Calculator(8, 3)
print(c.square())
print(c.exponent())