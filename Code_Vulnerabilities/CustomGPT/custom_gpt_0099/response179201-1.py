
def enterPass():
    x = input("Enter password (alpha or alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True
    else:
        print("Try again")
        return False

_try = 1
while _try <= 3:
    if enterPass():
        break
    _try += 1
