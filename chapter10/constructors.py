class Emp:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Emp is created!")

    def getDetails(self):
        print(f"The name of employee is {self.name}")
        print(f"The salary of employee is {self.salary}")
        print(f"The subunit of employee is {self.subunit}")

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")
    
    @staticmethod   # decorator to mark greet as a static method
    def greet():
        print("Good Morning, Mam")

    @staticmethod
    def time():
        print("The time is 4 PM")

Akriti = Emp("Akriti", 100, "Youtube")
Akriti.getDetails()
