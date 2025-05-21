 # 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.


# Define the custom exception InvalidAgeError
class InvalidAgeError(Exception):
    """Custom exception for invalid age input."""
    def __init__(self, message="Age must be 18 or older."):
        self.message = message
        super().__init__(self.message)

# Function to check the age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. Age must be at least 18.")
    else:
        return "Age is valid."

# Test the function with try...except to handle the custom exception
try:
    age = 16  # You can change this to test different ages
    result = check_age(age)
    print(result)
except InvalidAgeError as e:
    print(f"Error: {e}")
