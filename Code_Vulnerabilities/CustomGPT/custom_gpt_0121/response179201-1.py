
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Return True for a valid password
    else:
        print("Try again")
        return False  # Return False for an invalid password

_try = 1
max_attempts = 3

while _try <= max_attempts:
    if enterPass():  # Check if the password is valid
        break  # Exit loop if valid password is entered
    _try += 1

if _try > max_attempts:
    print("Exceeded maximum attempts.")
