
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Return True if valid
    else:
        print("Try again")
        return False  # Return False if invalid

_try = 1
while _try <= 3:
    if enterPass():  # Check if password is valid
        break  # Exit the loop if saved
    _try += 1
