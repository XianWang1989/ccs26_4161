
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Return True if the password is valid
    else:
        print("Try again")
        return False  # Return False if the password is invalid

_try = 1
success = False

while _try <= 3 and not success:
    success = enterPass()  # Call the function and check if it returns True
    _try += 1

if not success:
    print("You have exceeded the maximum attempts.")
