# 6. Constructors and Destructors

# Assignment:

# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).


#---------SOLUTION-----------#


class Logger:
    def __init__(self):
        print("Logger object has been created.")

    def __del__(self):
        print("Logger object is being destroyed.")

# Example usage
if __name__ == "__main__":
    log = Logger()  # Constructor is called here
    del log         # Destructor is explicitly called here (optional)

