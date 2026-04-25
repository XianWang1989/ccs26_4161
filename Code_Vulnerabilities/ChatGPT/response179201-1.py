
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Return True if the password is valid
    else:
        print("Try again")
        return False  # Return False for an invalid password

_try = 0
max_attempts = 3

while _try < max_attempts:
    if enterPass():  # Check if the password was valid
        break  # Exit the loop if valid password was entered
    _try += 1

if _try == max_attempts:
    print("Max attempts reached. Program quitting.")  # Inform the user they have reached the max attempts
