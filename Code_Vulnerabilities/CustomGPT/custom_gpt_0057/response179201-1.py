
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True
    else:
        print("Try again")
        return False

_try = 1
max_attempts = 3
while _try <= max_attempts:
    if enterPass():
        break
    _try += 1
