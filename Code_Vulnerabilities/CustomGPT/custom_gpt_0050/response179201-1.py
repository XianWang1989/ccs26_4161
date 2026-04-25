
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Return True if password is valid
    else:
        print("Try again")
        return False  # Return False if password is invalid

_try = 1
while _try <= 3:
    if enterPass():  # Call function and check for success
        break  # Exit the loop if password is valid
    _try += 1
