

class Emp:
    company = "Google"


    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")
    
    @staticmethod   # decorator to mark greet as a static method
    def greet():
        print("Good Morning, Mam")

Akriti = Emp()
Akriti.salary = 100000
Akriti.getSalary("Thanks!") # Employee.getSalary(Akriti)
Akriti.greet() # Employee.greet()