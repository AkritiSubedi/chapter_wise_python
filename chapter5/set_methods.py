# creating empty set
b = set()
print(type(b))

#adding values to an empty set
b.add(4)
b.add(5) # adding a value repeatedly does not changes a set
b.add(4)
b.add(5)
# you cannot add list in a set
# b.add([4,5,6]) 
# Accessing Elements
b.add((4,5,6))

print(b)
# length of the set
print(len(b)) # print the length of this set

b.remove(5)
# b.remove(15) # throws an error
print(b)
print(b.pop())
print(b)