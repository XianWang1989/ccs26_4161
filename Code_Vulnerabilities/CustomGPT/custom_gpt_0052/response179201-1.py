
def enterPass():
    x = input("Enter password (Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True
    else:
        print("Try again")
        return False

_try = 1
while _try <= 3:
    if enterPass():
        break  # Exit the loop if the password is valid
    _try += 1

if _try > 3:
    print("Too many attempts. Program exited.")
