
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicates a valid password
    else:
        print("Try again")
        return False  # Indicates an invalid password

_try = 1
while _try <= 3:
    if enterPass():
        break  # Exit loop if password is valid
    _try += 1

if _try > 3:
    print("Exceeded maximum attempts.")
