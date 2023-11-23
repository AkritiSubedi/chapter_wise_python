'''
    The game() function in a program lets a user play a game and 
    returns score as an int. 
'''

def game():
    return 44

score = game()

# Try to read the existing hiscore
try:
    with open("hiscore.txt", "r") as f:
        hiscore = int(f.read())
except FileNotFoundError:
    # If the file doesn't exist, initialize hiscore to 0
    hiscore = 0
except ValueError:
    # If the file contains invalid data, handle the error (e.g., set hiscore to 0)
    hiscore = 0

if score > hiscore:
    # Update the hiscore if the current score is higher
    with open("hiscore.txt", "w") as f:
        f.write(str(score))

print(f"Current Score: {score}, Hiscore: {hiscore}")
