
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate success
    else:
        print("Try again")
        return False  # Indicate failure

_try = 1
max_attempts = 3
success = False

while _try <= max_attempts and not success:
    success = enterPass()  # Call the function and update the success status
    _try += 1
