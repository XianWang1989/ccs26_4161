
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicates that the password is valid
    else:
        print("Try again")
        return False  # Indicates that the password is invalid

_try = 1
success = False
while (_try <= 3) and (not success):
    success = enterPass()
    _try += 1
