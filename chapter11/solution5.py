''' write a class vector representing a vector of n dimension.
    overload the + and * operator which calculates the sum and 
    the dot product of them.
'''

class Vector:
    def __init__(self, vec) -> None:
        self.vec = vec


    def __str__(self) -> str:
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i}a{index} +"
            index +=1
        return str1[:-1]
    
    def __add__(self, vec2):
        newlist = []
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] + vec2.vec[i])
        return Vector(newlist)

    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += (self.vec[i] * vec2.vec[i])
        return sum
    
v1 = Vector([4, 6])
v2 = Vector([1,6])
print(v1+v2)
print(v1*v2)