
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No Spaces'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate success
    else:
        print("Try again")
        return False  # Indicate failure

_try = 1
success = False

while _try <= 3 and not success:
    success = enterPass()  # Try to enter the password
    _try += 1
