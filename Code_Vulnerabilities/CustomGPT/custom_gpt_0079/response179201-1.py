
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Password is valid
    else:
        print("Try again")
        return False  # Password is invalid

_try = 1
max_attempts = 3
valid_password = False

while _try <= max_attempts and not valid_password:
    valid_password = enterPass()
    _try += 1

if not valid_password:
    print("Failed to enter a valid password after 3 attempts.")
