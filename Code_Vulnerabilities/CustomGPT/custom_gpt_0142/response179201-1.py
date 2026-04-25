
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate that the password was valid
    else:
        print("Try again")
        return False  # Indicate that the password was invalid


_try = 1
max_attempts = 3

while _try <= max_attempts:
    if enterPass():  # If valid password is entered
        break  # Exit the loop if the password is saved
    _try += 1

if _try > max_attempts:
    print("Maximum attempts reached, exiting.")
