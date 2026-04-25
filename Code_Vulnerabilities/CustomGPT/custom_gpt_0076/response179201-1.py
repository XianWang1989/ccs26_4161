
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    return x.isalnum()

_try = 1
while _try <= 3:
    if enterPass():
        print("Saved")
        break
    else:
        print("Try again")
        _try += 1
