# create class programmer for storing information of few programmers working at microsoft


class Programmer:
    company = "Microsoft"
    def __init__(self, name, product) :
        self.name = name
        self.product = product
    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and product is {self.product}")


Akriti = Programmer("Akriti", "Vs code")
Kriti = Programmer("Kriti", "GitHub")
Akriti.getInfo()
Kriti.getInfo()


        