
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

while _try <= max_attempts:
    if enterPass():  # Call function and check return value
        break  # Exit loop if password is valid
    _try += 1

if _try > max_attempts:
    print("Exceeded maximum attempts.")
