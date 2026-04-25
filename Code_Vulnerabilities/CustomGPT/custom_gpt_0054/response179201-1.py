
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate successful entry
    else:
        print("Try again")
        return False  # Indicate failure

_try = 1
max_attempts = 3
successful_entry = False

while _try <= max_attempts:
    successful_entry = enterPass()
    if successful_entry:
        break  # Exit the loop if the password is valid
    _try += 1

if not successful_entry:
    print("Exceeded maximum attempts.")
