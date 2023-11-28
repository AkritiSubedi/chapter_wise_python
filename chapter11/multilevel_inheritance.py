# 
class Person:
    country = "Nepal"
    def takeBreath(self):
        print("I am breathing...")

class Employee:
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreak(self):
        print("I am an Employee so I am luckily breathing..")


class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreak(self):
        print("I am an Programmer so I am luckily breathing..")

p = Person()
p.takeBreath()
# print(p.company) throws an error

e = Employee()
e.takeBreak()
print(e.company)

pr = Programmer()
pr.takeBreak()
print(pr.company)

    