
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate success
    else:
        print("Try again")
        return False  # Indicate failure

_try = 1
success = False

while _try <= 3 and not success:
    success = enterPass()  # Call the function and check for success
    _try += 1

if not success:
    print("Exceeded maximum attempts.")
