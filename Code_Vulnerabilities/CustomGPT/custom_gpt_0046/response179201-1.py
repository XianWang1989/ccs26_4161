
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate success
    else:
        print("Try again")
        return False  # Indicate failure

_try = 1
successful = False

while _try <= 3:
    successful = enterPass()
    if successful:  # Exit the loop if the password is valid
        break
    _try += 1

if not successful:
    print("Exceeded maximum attempts.")
