
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
    if enterPass():  # Check if the password was accepted
        break  # Exit the loop if successful
    _try += 1
