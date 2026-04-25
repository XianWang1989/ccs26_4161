
def enterPass():
    x = input("enter password Alpha or Alphanumeric! 'No_Space' :")
    if x.isalnum():
        print("saved")
        return True  # Return True if password is valid
    else:
        print("try again")
        return False  # Return False if password is invalid

_try = 1
while _try <= 3:
    if enterPass():  # Check if the password is valid
        break  # Exit the loop if valid password is entered
    _try += 1
