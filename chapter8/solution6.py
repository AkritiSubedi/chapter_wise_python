# function to remove a given word from a string and strip it at the same time
def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this= "     Hii How are you?  "
n = remove_and_split(this, "Hii")
print(n)
print(this)
print(this.strip()) # strip removes extra spaces
