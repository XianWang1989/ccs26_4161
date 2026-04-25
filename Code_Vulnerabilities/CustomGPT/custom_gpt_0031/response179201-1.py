
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicates success
    else:
        print("Try again")
        return False  # Indicates failure

_try = 0
while _try < 3:
    if enterPass():  # Call enterPass and check the result
        break  # Exit the loop if the password is valid
    _try += 1

if _try == 3:
    print("Max attempts reached. Program will exit.")
