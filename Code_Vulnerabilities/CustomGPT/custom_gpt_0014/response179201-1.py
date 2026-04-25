
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate success
    else:
        print("Try again")
        return False  # Indicate failure

try_count = 0
max_tries = 3
while try_count < max_tries:
    if enterPass():  # Call the function and check if it returned True
        break  # Exit the loop if the password is valid
    try_count += 1

if try_count == max_tries:
    print("Exceeded maximum attempts.")
