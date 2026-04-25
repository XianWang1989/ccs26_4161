
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate success
    else:
        print("Try again")
        return False  # Indicate failure

_try = 1
while _try <= 3:
    if enterPass():  # Check if the password is valid
        break  # Exit loop if valid
    _try += 1
