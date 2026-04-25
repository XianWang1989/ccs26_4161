
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Return True for valid input
    else:
        print("Try again")
        return False  # Return False for invalid input

_try = 1
while _try <= 3:
    if enterPass():  # If valid password is entered
        break  # Exit the loop
    _try += 1

if _try > 3:
    print("Exceeded maximum attempts.")
