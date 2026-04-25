
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space' ): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicates success
    else:
        print("Try again")
        return False  # Indicates failure

_try = 1
max_tries = 3

while _try <= max_tries:
    if enterPass():  # If True is returned, quit the loop
        break
    _try += 1
