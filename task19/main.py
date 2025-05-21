# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function




class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Set the factor to multiply with

    # Define the __call__() method to make instances callable like functions
    def __call__(self, value):
        return value * self.factor

# Create an instance of the Multiplier class with a factor of 5
multiply_by_5 = Multiplier(5)

# Test if the instance is callable using callable()
print(callable(multiply_by_5))  # Output: True

# Call the instance like a function, multiplying the input by 5
result = multiply_by_5(10)
print(result)  # Output: 50
