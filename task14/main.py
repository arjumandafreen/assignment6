# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.




class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}")


class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: employee is passed, not created here

    def display(self):
        print(f"Department: {self.dept_name}")
        self.employee.display()


# Independent Employee object
emp1 = Employee("Alice Smith", 101)

# Department has a reference to the existing Employee object
dept1 = Department("Human Resources", emp1)

# Display information
dept1.display()
