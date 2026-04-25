
def enterPass():
    x = input("enter password Alpha or Alphanumeric! 'No_Space' :")  # Updated to 'input()' for Python 3
    if x.isalnum():
        print("saved")
        return True  # Return True if password is valid
    else:
        print("try again")
        return False  # Return False if password is invalid

_try = 1
while _try <= 3:
    if enterPass():  # Check if the password is valid
        break  # Exit loop if password is saved
    _try += 1

if _try > 3:
    print("Too many attempts. Program exiting.")
