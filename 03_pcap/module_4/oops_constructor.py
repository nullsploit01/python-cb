class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        
    def display(self):
        print(f"Employee: {self.name}, ID: {self.emp_id}")
        
e1 = Employee("John", 12)
e1.display()

# Create a class BankAccount
# properties - account_holder, balance
# add a method - display_account_info()
# initialize that class 2 different times