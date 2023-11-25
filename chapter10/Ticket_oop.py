

class TicketForm:
    formType = "TicketForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Bus is {self.bus}")

akritiApplication = TicketForm()
akritiApplication.name = "Akriti"
akritiApplication.bus = "Samyukta Yatayat"
akritiApplication.printData()