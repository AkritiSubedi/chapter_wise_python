# 
class Person:

    country = "Nepal"
    def __init__(self) -> None:
        print("Initializing person...\n")

    def takeBreath(self):
        print("I am breathing...")

class Employee:
    company = "Honda"

    
    def __init__(self) -> None:
        super().__init__()
        print("Initializing Employee..\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
     
        print("I am an Employee so I am luckily breathing..")


class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        
        print(f"No salary to programmers")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Programmer so I am luckily breathing..")

# p = Person()
# p.takeBreath()


e = Employee()
# e.takeBreath()


# pr = Programmer()
# pr.takeBreath()


    