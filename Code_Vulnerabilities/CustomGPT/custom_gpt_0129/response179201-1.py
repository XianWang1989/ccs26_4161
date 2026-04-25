
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")  # Use input() in Python 3
    if x.isalnum():
        print("saved")
        return True  # Indicate success
    else:
        print("try again")
        return False  # Indicate failure

_try = 1
while _try <= 3:
    if enterPass():  # Call function and check if it returns True
        break  # Exit the loop if the password is valid
    _try += 1
