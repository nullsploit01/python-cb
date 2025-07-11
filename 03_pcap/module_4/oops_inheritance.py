class Animal:
    def speak(self):
        print("Animal Sound")
        
class Dog(Animal):
    def speak(self):
        print("Woof!")
            
class Cat(Animal):
    def speak(self):
        print("Meow!")
        
pets = [Dog(), Cat()]

for pet in pets:
    pet.speak()
    
d = Dog()
print(isinstance(d, Dog))
print(isinstance(d, Animal))

# A base class named Shape
# - Have a method called area()
# 2 subclasses called Square and Circle
# - Both of them will have area