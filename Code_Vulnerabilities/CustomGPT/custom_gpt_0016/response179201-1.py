
def enterPass():
    x = input("Enter password Alpha or Alphanumeric! 'No_Space': ")
    if x.isalnum():
        print("Saved")
        return True  # Return True if valid password
    else:
        print("Try again")
        return False  # Return False if invalid

_attempts = 1
while _attempts <= 3:
    if enterPass():  # Call the function and check its return value
        break  # Exit the loop if the password is valid
    _attempts += 1

if _attempts > 3:  # Notify user after 3 failed attempts
    print("Maximum attempts reached. Exiting...")
