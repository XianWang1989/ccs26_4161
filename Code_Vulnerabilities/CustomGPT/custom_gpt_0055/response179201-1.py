
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Successful input
    else:
        print("Try again")
        return False  # Input failed

_try = 1
while _try <= 3:
    if enterPass():  # If enterPass returns True
        break  # Exit loop on success
    _try += 1
