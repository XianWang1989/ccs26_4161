
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate successful entry
    else:
        print("Try again")
        return False  # Indicate unsuccessful entry

_try = 1
max_attempts = 3
valid_password = False

while _try <= max_attempts:
    valid_password = enterPass()
    if valid_password:
        break  # Exit the loop if the password is valid
    _try += 1

if not valid_password:
    print("Max attempts reached. Program exiting.")
