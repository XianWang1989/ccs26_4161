
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Return True to indicate success
    else:
        print("Try again")
        return False  # Return False to indicate failure

_try = 1
while _try <= 3:
    if enterPass():  # If the function returns True, break the loop
        break
    _try += 1
