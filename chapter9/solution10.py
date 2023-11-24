# write a program to wipe out the contents of a file using python
import os
filename = "sample.txt"
with open(filename, "w") as f:
    f.write("")


oldname = "copy.txt "
newname = "renamed_by_copy1.txt"
with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)