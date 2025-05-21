# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.


# Define the class decorator
def add_greeting(cls):
    # Define the greet method to be added
    def greet(self):
        return "Hello from Decorator!"
    
    # Add the greet method to the class
    cls.greet = greet
    return cls

# Define the Person class and apply the decorator
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        return f"My name is {self.name}"

# Create an instance of the Person class
person = Person("Alice")

# Call the greet method added by the decorator
print(person.greet())  # Output: Hello from Decorator!

# Call the introduce method
print(person.introduce())  # Output: My name is Alice
