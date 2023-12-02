# class method is bound to class and not the object of the class
class Employee:
    company = " Camel"
    salary = 100
    location = "Kathmandu"

    @classmethod   # used to create a class method
    def changeSalary(cls, sal):
        cls.salary = sal

    #def changeSalary(self, sal):
    #   self.__class__.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(445)
print(e.salary)
print(Employee.salary)