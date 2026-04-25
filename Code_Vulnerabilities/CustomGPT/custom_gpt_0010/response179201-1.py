
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate success
    else:
        print("Try again")
        return False  # Indicate failure

_try = 1
max_attempts = 3

while _try <= max_attempts:
    if enterPass():
        break  # Exit the loop if password is valid
    _try += 1
