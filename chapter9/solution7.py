# program to find out line number where python is present from solution 6
content = True
i = 1
with open("log.txt") as f:
    while content:

        content = f.readline()
        if'python' in content.lower():
            print(content)
            print ("yes python is present on line number {i}")
            print(i)
        i+=1

