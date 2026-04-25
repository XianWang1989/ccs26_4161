
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True
    else:
        print("Try again")
        return False

_try = 1
while _try <= 3:
    if enterPass():
        break  # Exit the loop on successful entry
    _try += 1

if _try > 3:
    print("Exceeded maximum attempts.")
