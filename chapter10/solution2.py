# Class calculator capablee of finding square, cube and squareroot of a number.

class Calculator:
    def __init__(self, num) -> None:
        self.number = num
    
    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    def squareRoot(self):
        print(f"The value of {self.number} squareRoot is {self.number **2}")


    def cube(self):
        print(f"The value of {self.number} cube is {self.number **3}")


a = Calculator(3)
a.squareRoot()
a.cube()
a.square()