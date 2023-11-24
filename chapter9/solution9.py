# # program to find out whether a file is identical and matches content of another file


file1 = "copy.txt"
file2 = "this.txt"


with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2= f.read()

if f1==f2:
    print("files are identical")

else:
    print("files are not identical")