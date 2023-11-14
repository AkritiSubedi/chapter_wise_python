'''A spam comment is defined as a text containing following keywords:
"Make a lot of money", "buy now","subscribe this", "click this", 
write a program to detect these spams
'''
text = input("Enter the text")
spam = False

if("Make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("Subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")