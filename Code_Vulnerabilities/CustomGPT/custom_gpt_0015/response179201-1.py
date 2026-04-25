
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Return True if the password is valid
    else:
        print("Try again")
        return False  # Return False if the password is invalid

_try = 1
while _try <= 3:
    if enterPass():  # Check if the password was accepted
        break  # Exit the loop if successful
    _try += 1

if _try > 3:
    print("Exceeded the maximum attempts!")
