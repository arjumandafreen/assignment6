# 3. Public Variables and Methods

# Assignment:

# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

   #---------------SOLUTION-------------------------------------#



class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):  # Public method
        print(f"The {self.brand} car has started.")

# Example usage
my_car = Car("Toyota")

# Accessing public variable and method from outside the class
print("Brand:", my_car.brand)
my_car.start()
