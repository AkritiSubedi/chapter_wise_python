class Employee:
    company = "Samsung"
    salary = 9500
    salarybonus = 500
    # totalSalary = 10,000

    @property 
    # the method name with @property decorator is called getter method
    def totalSalary(self):
        return self.salary + self.salarybonus
    
    @totalSalary.setter  
    def totalSalary(self, val):
        self.salarybonus = val - self.salary


e = Employee()
print(e.totalSalary)
e.totalSalary = 10000
print(e.salary)
print(e.salarybonus)
