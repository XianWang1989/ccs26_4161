
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate success
    else:
        print("Try again")
        return False  # Indicate failure

# Allow a maximum of 3 attempts
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    if enterPass():
        break  # Exit loop on success
    attempts += 1

if attempts == max_attempts:
    print("Maximum attempts reached. Exiting...")
