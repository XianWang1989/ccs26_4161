
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True
    else:
        print("Try again")
        return False

_try = 1
success = False
while _try <= 3 and not success:
    success = enterPass()
    _try += 1
