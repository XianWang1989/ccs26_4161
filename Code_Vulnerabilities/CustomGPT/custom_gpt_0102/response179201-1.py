
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate success
    else:
        print("Try again")
        return False  # Indicate failure

_try = 1
max_attempts = 3

while _try <= max_attempts:
    if enterPass():  # Check if the password is valid
        break  # Exit the loop if successful
    _try += 1

if _try > max_attempts:
    print("Maximum attempts reached. Exiting.")
