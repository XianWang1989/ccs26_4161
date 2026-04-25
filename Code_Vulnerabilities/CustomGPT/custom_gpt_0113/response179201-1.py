
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No Space'): ")  # Use input() for Python 3
    if x.isalnum():
        print("Saved")
        return True  # Returning True if the password is valid
    else:
        print("Try again")
        return False  # Returning False if the password is not valid

_try = 1
while _try <= 3:
    if enterPass():  # Call the function and check the return value
        break  # Exit the loop if the password is valid
    _try += 1
