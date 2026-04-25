
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Return True when password is valid
    else:
        print("Try again")
        return False  # Return False when password is not valid

_try = 1
max_attempts = 3

while _try <= max_attempts:
    if enterPass():  # Check if the function returned True
        break  # Exit the loop if the password is valid
    _try += 1

if _try > max_attempts:
    print("Too many attempts. Program quitting.")
