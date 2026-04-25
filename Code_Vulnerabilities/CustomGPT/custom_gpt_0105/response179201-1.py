
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicates successful entry
    else:
        print("Try again")
        return False  # Indicates failure

_try = 1
while _try <= 3:
    if enterPass():  # Check if password is valid
        break  # Exit loop if saved
    _try += 1

if _try > 3:
    print("Maximum attempts reached. Exiting.")
