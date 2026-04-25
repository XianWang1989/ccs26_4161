
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Password is valid
    else:
        print("Try again")
        return False  # Password is invalid

_try = 1
while _try <= 3:
    if enterPass():  # Check for valid password
        break  # Exit the loop if valid
    _try += 1
