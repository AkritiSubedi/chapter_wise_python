# Multiple inheritance occurs when the child class inherits from more than one parent class


class Emp:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "Fiverr"
    level = 2

    def upgradeLevel(self):
        self.level = self.level +1

class Programmer(Emp, Freelancer): # gives priority to first class i.e emp
    name = "Akriti"

p = Programmer()
p.upgradeLevel()
print(p.level)