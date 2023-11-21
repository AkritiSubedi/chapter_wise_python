# program using function to convert celsus to fahreheit

def farh(cel):
    return (cel *(9/5)) + 32 # to convert celsus to fahreheit

c = 45
f = farh(c)
print("Fahreheit temperature is " + str(f))