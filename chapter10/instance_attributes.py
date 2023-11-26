class Employee:
    company = "Google"
    salary = 1000

kriti = Employee()

aakriti = Employee()

# creating instance attribute salary for both objects
kriti.salary = 11500   
aakriti.salary = 1500


print(kriti.salary)
print(aakriti.salary)