# 8. The super() Function

# Assignment:

# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor. 

# Create an instance of Teacher and print the name and subject.

#--------------SOLUTION-------------------------------#
# Base class
class Person:
    def __init__(self, name):
        self.name = name  # Initialize name

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of the Person class
        self.subject = subject  # Initialize subject

# Create an instance of Teacher
teacher = Teacher("Mr. Smith", "Mathematics")

# Print name and subject
print("Name:", teacher.name)
print("Subject:", teacher.subject)

