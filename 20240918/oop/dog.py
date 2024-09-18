class Dog:
    # Class attribute
    species = "Canis lupus familiaris"    
    # Constructor (initializer) method
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}."

# Creating an object (instance of the class)
dog1 = Dog("Buddy", 3)
print(dog1.description())  # Output: Buddy is 3 years old.
print(dog1.speak("Woof!"))  # Output: Buddy says Woof!

fork = Dog("Fork", 5)
print(fork.description())  # Output: Fork is 5 years old.
print(fork.speak("Woof!"))  # Output: Fork says Woof!

dogs = [dog1, fork]
from functools import reduce 
#reduce syntax
#reduce(<func>, iterable, init_value)
ages_sum = reduce((lambda s, dog: s + dog.age), dogs, 0)
print(ages_sum)

