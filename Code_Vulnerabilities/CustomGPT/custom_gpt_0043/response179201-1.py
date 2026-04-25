
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Return True if password is valid
    else:
        print("Try again")
        return False  # Return False if password is invalid

_try = 1
password_accepted = False  # Variable to track if password is accepted

while (_try <= 3) and (not password_accepted):
    password_accepted = enterPass()  # Call function and check if it's valid
    _try += 1

if not password_accepted:
    print("Maximum attempts reached. Program exiting.")
