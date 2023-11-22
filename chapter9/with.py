'''best way to open and close the file automatically 
is the with statements'''

with open('another.txt', 'r') as f:
    a = f.read()  # dont need to write f.close() as it is done automatically
with open('another.txt', 'w') as f:
    a = f.write("me")
print(a)