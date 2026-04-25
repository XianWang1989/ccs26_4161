
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Return True if the password is accepted
    else:
        print("Try again")
        return False  # Return False if the password is not accepted

_try = 1
while _try <= 3:
    if enterPass():  # Call enterPass() and check if True is returned
        break  # Exit the loop if the password is accepted
    _try += 1
