
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Return True if password is valid
    else:
        print("Try again")
        return False  # Return False if password is invalid

_try = 1
while _try <= 3:
    if enterPass():  # Check if password is valid
        break  # Exit loop if valid password
    _try += 1

if _try > 3:
    print("Exceeded maximum attempts.")
