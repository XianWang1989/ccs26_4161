
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Password is valid
    else:
        print("Try again")
        return False  # Password is not valid

_try = 1
while _try <= 3:
    if enterPass():  # Call the function and check if it returned True
        break  # Exit the loop if the password was saved successfully
    _try += 1

if _try > 3:
    print("Exceeded the maximum number of attempts.")
