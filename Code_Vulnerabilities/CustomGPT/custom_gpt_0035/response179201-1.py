
def enterPass():
    x = input("Enter password Alpha or Alphanumeric! 'No_Space': ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate success
    else:
        print("Try again")
        return False  # Indicate failure

_try = 1
max_attempts = 3
success = False

while _try <= max_attempts:
    success = enterPass()  # Call the function
    if success:  # Check if the password was valid
        break  # Exit loop on success
    _try += 1  # Increment attempt count
