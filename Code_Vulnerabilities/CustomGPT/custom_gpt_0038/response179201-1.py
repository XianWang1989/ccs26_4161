
def enterPass():
    while True:
        x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
        if x.isalnum():
            print("Saved")
            return True  # Indicate success
        else:
            print("Try again")

_try = 1
while _try <= 3:
    if enterPass():
        break  # Exit the loop if the password is saved
    _try += 1
else:
    print("Too many attempts. Program quitting.")
