
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate success
    else:
        print("Try again")
        return False  # Indicate failure

_try = 1
while _try <= 3:
    if enterPass():  # Call enterPass and check its return value
        break  # Exit loop if password is valid
    _try += 1  # Increment attempt count

if _try > 3:
    print("Exceeded maximum attempts. Program exits.")
