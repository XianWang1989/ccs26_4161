
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Return True when password is valid
    else:
        print("Try again")
        return False  # Return False when password is not valid


try_count = 1
max_tries = 3

while try_count <= max_tries:
    if enterPass():  # If the password is valid
        break  # Break the loop
    try_count += 1
