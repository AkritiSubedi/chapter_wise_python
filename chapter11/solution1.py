'''create a class c2d vector and use it to 
create another class representing a 3-d vector'''

class C2dVec:
    def __init__(self, i, j) -> None:
        self.icap = i
        self.jcap = j
    
    def __str__(self) -> str:
        return f"{self.icap}i + {self.jcap}j"

class C3dVec(C2dVec):
    def __init__(self, i, j, k) -> None:
        super().__init__(i,j)
        self.kcap = k

    def __str__(self) -> str:
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"


v2d = C2dVec(11,3)
v3d = C3dVec(1,9,5)
print(v2d)
print(v3d)