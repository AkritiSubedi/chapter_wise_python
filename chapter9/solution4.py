'''# write a file contains "Donkey" ,ultiple times. you need to write
 a program which replaces this word with "$%^@$^#" 
 by updating the same file'''


with open("sample.txt") as f:
    content = f.read()

content = content.replace("donkey" , "$%^@$^#")

with open("sample.txt", "w") as f:
    f.write(content)


