
def enterPass():
    x = raw_input("Enter password Alpha or Alphanumeric! 'No_Space' : ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate successful password entry
    else:
        print("Try again")
        return False  # Indicate failure

_try = 1
while _try <= 3:
    if enterPass():  # Check the return value
        break  # Exit the loop if password is saved
    _try += 1
