# program to find out whether a given username contains less than 10 characters or not
def check_username_length(username):
    # Check if the length of the username is less than 10 characters
    if len(username) < 10:
        return True
    else:
        return False

# Example usage:
username = input("Enter a username: ")

if check_username_length(username):
    print("Username contains less than 10 characters.")
else:
    print("Username contains 10 or more characters.")
