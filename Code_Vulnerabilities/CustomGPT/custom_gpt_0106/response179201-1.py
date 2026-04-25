
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate success
    else:
        print("Try again")
        return False  # Indicate failure

_try = 0
while _try < 3:
    if enterPass():  # Check if the password is valid
        break  # Exit the loop if valid password is entered
    _try += 1

if _try == 3:
    print("Too many attempts. Program quitting.")
