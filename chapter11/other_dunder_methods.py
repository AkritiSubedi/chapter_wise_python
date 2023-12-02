class Number:
    def __init__(self, num) -> None:
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num
    
    def __mul__(self, num2):
        print("Lets multiply")
        return self.num * num2.num
    
    def __str__(self) -> str:
        return f"DecimalNumber: {self.num}"
    

    def __len__(self):
        return 2

# n1 = Number(44)
# n2 = Number(60)
# sum = n1 + n2
# mul = n1 * n2
# print(sum)
# print(mul)

n = Number(99)
print(n)
print(len(n))