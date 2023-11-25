class Employee:
    company = "Google"
    salary = 1000

kriti = Employee()

akriti = Employee()

# creating instance attribute salary for both objects
kriti.salary = 11500   
akriti.salary = 1500


print(kriti.salary)
print(akriti.salary)