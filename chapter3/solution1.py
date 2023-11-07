# display user input name followed by good afternoon using input() function
name = input("Enter your name: ")
print("Good Afternoon, " + name)


# letter template
letter = '''Dear <|NAME|>
    Greetings from ABC coding house. I am happy to tell you about your selection.

    You are selected !
    Enjoy your day
    Have a great day ahead !
    Thanks and regards,
    Bill
    Date: <|DATE|>
'''
name = input("Enter your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)