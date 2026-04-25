
def enterPass():
    x = input("Enter password Alpha or Alphanumeric! 'No_Space': ")  # Use input() instead of raw_input()
    if x.isalnum():
        print("Saved")
        return True  # Return True if the password is valid
    else:
        print("Try again")
        return False  # Return False if the password is invalid

_try = 1
while _try <= 3:
    if enterPass():  # Check if the password was saved (valid)
        break  # Exit the loop if a valid password is entered
    _try += 1
