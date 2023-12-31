'''
Write a class train which has methods to book a ticket, 
get status(no of seats) and get fare information of trains running 
under gateways
'''


class Train:
    def __init__(self, name, fare, seats) -> None:
        self.name = name
        self.fare = fare
        self.seats = seats
        
    def getStatus(self):
        print("**********")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("**********")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print("Your Ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats -1
        else:
            print("Sorry this train is full ! Kindly check later")
    def cancelTickets(self, seatNo):
        pass

intercity = Train("Intercity Express: 14050", 90, 300)
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()