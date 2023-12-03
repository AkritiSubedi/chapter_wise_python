'''
create a class pets from a class animals and further create
class dog from pets. Add a method bark to classs dog.
'''

class Animals:
    animalType = "Mammal"

class Pets:  
    color = "White"

class Dog:  
    @staticmethod
    def bark():
        print("how how")

d = Dog()
d.bark()
