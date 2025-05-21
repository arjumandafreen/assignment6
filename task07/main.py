# 7. Access Modifiers: Public, Private, and Protected

# Assignment:

# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document
# what happens.
#-------------------SOLUTION-----------------#
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            # Public variable
        self._salary = salary       # Protected variable
        self.__ssn = ssn            # Private variable

# Create an object of the Employee class
emp = Employee("Alice", 75000, "123-45-6789")

# Accessing public variable
print("Public (name):", emp.name)  # ✅ Works fine

# Accessing protected variable
print("Protected (_salary):", emp._salary)  # ✅ Works, but should be accessed with caution

# Accessing private variable directly
try:
    print("Private (__ssn):", emp.__ssn)  # ❌ Raises AttributeError
except AttributeError as e:
    print("Private (__ssn): Cannot access directly -", e)

# Accessing private variable using name mangling
print("Private (__ssn) via name mangling:", emp._Employee__ssn)  # ✅ Works, but not recommended
