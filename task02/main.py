# 2. Using cls
# Assignment:02

# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

#-----------------SOLUTION------------------------------#


class Counter:
    count = 0  # Class variable to track number of objects

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

# Example usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.display_count()
