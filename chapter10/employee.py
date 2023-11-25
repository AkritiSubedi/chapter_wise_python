# class attributes

class Employee:
    company = "Google"
    salary = "1111"

# object instantiation
kriti = Employee() 

akriti = Employee()
kriti.salary = 11500   # instance attributes
akriti.salary = 1500

print(akriti.company)
print(kriti.company)
Employee.company = "Youtube"   # changing class attribute
print(kriti.company)
print(akriti.company)
print(kriti.salary)
print(akriti.salary)