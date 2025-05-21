# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.


#--------------Solution-----------------------------------------#

# Engine class
class Engine:
    def start(self):
        return "Engine started."

# Car class using composition
class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car "has-a" Engine

    def start_car(self):
        return self.engine.start()  # Accessing Engine method via Car

# Example usage
my_engine = Engine()
my_car = Car(my_engine)

print(my_car.start_car())  # Output: Engine started.
