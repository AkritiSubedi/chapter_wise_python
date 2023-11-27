'''
create a classs with class attribute a;
create an abject from it and set a directly using object.a = 0.
Does this change the class attribute? ans: No it doesnot

'''

class Sample:
    a = "Akriti"

obj = Sample()
obj.a = "Kriti"

print(Sample.a)
print(obj.a)