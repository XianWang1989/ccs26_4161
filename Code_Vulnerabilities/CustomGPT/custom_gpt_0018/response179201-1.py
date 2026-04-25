
def enterPass():
    x = input("Enter password Alpha or Alphanumeric! 'No_Space': ")
    if x.isalnum():
        print("Saved!")
        return True  # Return True for a valid password
    else:
        print("Try again.")
        return False  # Return False for an invalid password

_try = 1
while _try <= 3:
    if enterPass():  # Check if the password is valid
        break  # Exit the loop if the password is valid
    _try += 1

if _try > 3:
    print("Too many attempts.")
