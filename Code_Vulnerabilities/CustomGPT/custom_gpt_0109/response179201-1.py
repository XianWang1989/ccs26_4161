
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate successful input
    else:
        print("Try again")
        return False  # Indicate failure

_try = 1
while _try <= 3:
    if enterPass():  # Call the function and check if it returned True
        break  # Exit the loop if the password is valid
    _try += 1
