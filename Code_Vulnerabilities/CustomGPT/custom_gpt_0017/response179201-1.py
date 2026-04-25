
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Return True if valid
    else:
        print("Try again")
        return False  # Return False if invalid

_try = 1
max_attempts = 3

while _try <= max_attempts:
    if enterPass():  # Call enterPass and check return value
        break  # Exit loop if password is saved
    _try += 1
