
def enterPass():
    x = input("Enter password (Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate success
    else:
        print("Try again")
        return False  # Indicate failure

try_count = 1
while try_count <= 3:
    if enterPass():  # Call enterPass and check if it returns True
        break  # Exit the loop if the password is valid
    try_count += 1

if try_count > 3:
    print("Max attempts reached. Exiting.")
