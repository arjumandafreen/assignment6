# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.



class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    # @property is used to get the value of _price
    @property
    def price(self):
        return self._price

    # @price.setter is used to set the value of _price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    # @price.deleter is used to delete _price
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Create a Product object
product = Product(100)

# Access the price using the getter
print(f"Price: {product.price}")  # Output: 100

# Update the price using the setter
product.price = 150
print(f"Updated Price: {product.price}")  # Output: 150

# Attempt to set a negative price (will raise ValueError)
try:
    product.price = -50
except ValueError as e:
    print(e)  # Output: Price cannot be negative.

# Delete the price using the deleter
del product.price  # Output: Deleting price...
