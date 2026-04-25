
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate success
    else:
        print("Try again")
        return False  # Indicate failure

_try = 1
while _try <= 3:
    if enterPass():  # Check for a successful entry
        break  # Exit the loop if the password is valid
    _try += 1

if _try > 3:
    print("Exceeded attempts. Program will exit.")
