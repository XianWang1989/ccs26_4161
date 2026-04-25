
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate the password was valid
    else:
        print("Try again")
        return False  # Indicate the password was invalid

_try = 1
while _try <= 3:
    if enterPass():  # Call the function and check the return value
        break  # Exit the loop if the password is valid
    _try += 1

if _try > 3:
    print("Exceeded maximum attempts")
