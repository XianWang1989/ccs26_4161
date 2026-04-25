
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicates that the password is valid
    else:
        print("Try again")
        return False  # Indicates that the password is invalid

_try = 1
while _try <= 3:
    if enterPass():  # Call the function and check if the password is valid
        break  # Exit the loop if the password is valid
    _try += 1
