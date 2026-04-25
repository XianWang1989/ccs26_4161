
def enterPass():
    x = input("Enter password Alpha or Alphanumeric! 'No_Space' : ")
    if x.isalnum():
        print("Saved")
        return True  # Return True if the input is valid
    else:
        print("Try again")
        return False  # Return False if the input is invalid

_try = 1
max_attempts = 3

while _try <= max_attempts:
    if enterPass():  # Call the function, if it returns True, exit loop
        break
    _try += 1

if _try > max_attempts:
    print("Exceeded maximum attempts.")
