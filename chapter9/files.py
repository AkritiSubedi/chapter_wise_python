# file I/O

#f = open('sample.txt', 'r')
f = open('sample.txt')  # by default the mode is read i.e r
# data = f.read() # read its contents
data = f.read(10) # read 10 characters only
print(data)
f.close()