
def enterPass():
    x = input("Enter password Alpha or Alphanumeric! 'No_Space': ")
    return x.isalnum()

_try = 1
while _try <= 3:
    if enterPass():
        print("Saved")
        break  # Exit the loop if the password is valid
    else:
        print("Try again")
    _try += 1

if _try > 3:
    print("Maximum attempts reached. Program will quit.")
