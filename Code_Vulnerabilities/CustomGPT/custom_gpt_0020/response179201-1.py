
def enterPass():
    x = input("Enter password Alpha or Alphanumeric! 'No_Space' : ")
    if x.isalnum():
        print("Saved")
        return True  # Return True if password is valid
    else:
        print("Try again")
        return False  # Return False if password is invalid

_try = 0
max_attempts = 3

while _try < max_attempts:
    if enterPass():  # If password is valid
        break  # Exit the loop
    _try += 1

if _try == max_attempts:
    print("Exceeded maximum attempts. Please try again later.")
