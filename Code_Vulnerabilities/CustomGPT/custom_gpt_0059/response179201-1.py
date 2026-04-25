
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate successful entry
    else:
        print("Try again")
        return False  # Indicate failed entry

_try = 1
while _try <= 3:
    if enterPass():  # If the password is valid, break the loop
        break
    _try += 1
