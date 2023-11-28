# Inheritance is a way of creating a new class from an existing class


class Emp:
    company = "Google"

    def showDetails(self):
        print("This is an Employee")

class Programmer(Emp):
        language = "Python"
        company = "Youtube"

        def getLanguage(self):
            print(f"The language is {self.language}")

        def showDetails(self):
            print("This is an Programmer")

e = Emp()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)

