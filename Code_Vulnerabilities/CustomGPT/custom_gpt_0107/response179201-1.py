
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicates success
    else:
        print("Try again")
        return False  # Indicates failure

_try = 1
while _try <= 3:
    if enterPass():
        break  # Exit the loop if password is valid
    _try += 1
