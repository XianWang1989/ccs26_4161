
def enterPass():
    x = input("Enter password Alpha or Alphanumeric! 'No_Space' : ")
    return x.isalnum()

_try = 1
success = False

while _try <= 3:
    if enterPass():
        print("Saved")
        success = True
        break  # Exit the loop on successful entry
    else:
        print("Try again")
    _try += 1

if not success:
    print("Reached maximum attempts. Exiting.")
