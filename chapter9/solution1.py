''' program to read text from given file 'poems.txt' 
and find out whether it contains word 'twinkle'''


f = open('poems.txt')
t = f.read()
if 'twinkle' in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")

f.close()