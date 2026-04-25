
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate success
    else:
        print("Try again")
        return False  # Indicate failure

_try = 1
while _try <= 3:
    if enterPass():  # Call function and check return value
        break  # Exit loop if password was valid
    _try += 1
