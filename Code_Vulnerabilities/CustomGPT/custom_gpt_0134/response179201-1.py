
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Return True if password is valid
    else:
        print("Try again")
        return False  # Return False if password is invalid

_try = 0  # Initialize attempt counter
max_attempts = 3

while _try < max_attempts:
    if enterPass():  # Call the function and check its return value
        break  # Exit the loop if the password is valid
    _try += 1  # Increment attempt counter

if _try == max_attempts:
    print("Maximum attempts reached. Exiting.")
