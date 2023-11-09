# program to accept marks of 6 students and display them in a sorted manner
marks1 = int(input("Enter Marks for Student Number 1: "))
marks2 = int(input("Enter Marks for Student Number 2: "))
marks3 = int(input("Enter Marks for Student Number 3: "))
marks4 = int(input("Enter Marks for Student Number 4: "))
marks5 = int(input("Enter Marks for Student Number 5: "))
marks6 = int(input("Enter Marks for Student Number 6: "))

myList = [marks1, marks2, marks3, marks4, marks5, marks6]
myList.sort()
print(myList)


