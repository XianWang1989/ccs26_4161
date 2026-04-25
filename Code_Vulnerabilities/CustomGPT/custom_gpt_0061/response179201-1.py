
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate success
    else:
        print("Try again")
        return False  # Indicate failure

try_count = 1
while try_count <= 3:
    if enterPass():  # If the password was successfully saved
        break  # Exit the loop
    try_count += 1
