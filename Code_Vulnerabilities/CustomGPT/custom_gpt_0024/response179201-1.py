
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Signal that the password is valid
    else:
        print("Try again")
        return False  # Signal that the password is invalid

_try = 1
while _try <= 3:
    if enterPass():  # If the password is valid
        break  # Exit the loop
    _try += 1
