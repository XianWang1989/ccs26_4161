
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space') : ")  # Use input() for Python 3
    if x.isalnum():
        print("Saved")
        return True  # Return True for a successful password
    else:
        print("Try again")
        return False  # Return False for an unsuccessful attempt

_try = 1
while _try <= 3:
    if enterPass():  # If a valid password is entered, exit the loop
        break  # Exit the loop if password is saved
    _try += 1

if _try > 3:
    print("Exceeded maximum attempts.")
