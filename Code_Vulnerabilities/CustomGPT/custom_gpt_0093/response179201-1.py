
def enter_pass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate success
    else:
        print("Try again")
        return False  # Indicate failure

_try = 1
while _try <= 3:
    if enter_pass():  # Call the function and check the return value
        break  # Exit the loop if the password is valid
    _try += 1
