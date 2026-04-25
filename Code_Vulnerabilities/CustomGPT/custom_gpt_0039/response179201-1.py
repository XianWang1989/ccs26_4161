
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate successful entry
    else:
        print("Try again")
        return False  # Indicate failure

_try = 0
max_tries = 3

while _try < max_tries:
    if enterPass():  # If True, exit the loop
        break
    _try += 1
