# program to write a log file and find out whether it contains 'python'

with open("log.txt") as f:
    content = f.read().lower()

if 'python' in content:
    print ("yes python is present")

else:
    print("No python is not present")