""""
'''
3.
'''
class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of Rs.{amount}successful.")
        else:
            print("Invalid deposit amount.")

    def withdrawal(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw of Rs. {amount} successful.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def bank_fees(self):
        fees = 0.05 * self.balance
        self.balance -= fees
        print(f"Bank fees of Rs.{fees} applied.")

    def display(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Account Holder: {self.name}")
        print(f"Balance: Rs. {self.balance}")


account1 = BankAccount(accountNumber=123456, name="john doe", balance=1000)

account1.display()
account1.deposit(500)
account1.withdrawal(200)
account1.bank_fees()

account1.display()
"""







"""
"""
1.
"""
class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable


class_namespace = dir(MyClass)
print("Namespace of MyClass:")
print(class_namespace)

obj = MyClass(instance_variable="I am an instance variable")


instance_namespace = dir(obj)
print("\nNamespace of the instance:")
print(instance_namespace)
"""










'''
2.
'''


class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student_instance = Student(student_id=1, student_name="John Doe")

print("Attributes and values before removal:")
print("Student ID:", student_instance.student_id)
print("Student Name:", student_instance.student_name)

student_instance.student_class = "Class 10"

print("\nAttributes and values after adding student_class:")
print("Student ID:", student_instance.student_id)
print("Student Name:", student_instance.student_name)
print("Student Class:", student_instance.student_class)

del student_instance.student_name

print("\nAttributes and values after removing student_name:")
print("Student ID:", student_instance.student_id)

print("Student Class:", student_instance.student_class)
