''' Arithmetic operators => -, +, *, / etc
    Assignment operators => =, +=, -= etc
    Comparision operators => ==, >, >=, <, != etc
    Logical operators => and or not
    '''
a = 35
b = 49

# Arithmetic operators
print("The value of 35 + 49 is ", a + b)
print("The value of 35 - 49 is ", a - b)
print("The value of 35 * 49 is ", a * b)
print("The value of 35 / 49 is ", a / b)

# Assignment operators
a = 35
a -= 12
# a *= 12
# a /= 12
# a += 12
print("Assignment operators becomes :", a)

# Comparision operators
b = (4>7)
# b = (14!=7)
# b = (14>=7)
# b = (14<=7)
# b = (14==7)
print(b)

# Logical operators
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 and bool2 is", (bool1 or bool2))
print("The value of bool1 and bool2 is", (not bool2))
