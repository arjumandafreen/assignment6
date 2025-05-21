# 4. Class Variables & Class Methods

# Create a class Bank with a class variable bank_name . Add a class method change_bank_name(cls, name)that allows changing the bank_name. Show that it affects all instances.



#--------------------SOLUTION-----------------------#
class Bank:
    # Class variable
    bank_name = "Old Bank Name"

    def __init__(self, customer_name):
        self.customer_name = customer_name

    # Class method to change the class variable
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display_info(self):
        print(f"Customer: {self.customer_name}, Bank: {Bank.bank_name}")


# Create instances
customer1 = Bank("Alice")
customer2 = Bank("Bob")

# Display initial bank names
print("Before changing bank name:")
customer1.display_info()
customer2.display_info()

# Change bank name using class method
Bank.change_bank_name("New Horizon Bank")

# Display updated bank names (should affect all instances)
print("\nAfter changing bank name:")
customer1.display_info()
customer2.display_info()

