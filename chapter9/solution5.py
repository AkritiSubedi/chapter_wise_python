# repeat solution 4 program for list of such words to be censored
words = ["donkey", "monkey"]

with open("sample.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word , "$%^@$^#")
    with open("sample.txt", "w") as f:
        f.write(content)