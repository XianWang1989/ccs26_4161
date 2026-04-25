
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")  # Use input() for Python 3
    if x.isalnum():
        print("Saved")
        return True  # Indicate success
    else:
        print("Try again")
        return False  # Indicate failure

_try = 0
max_attempts = 3

while _try < max_attempts:
    if enterPass():  # Check if password is valid
        break  # Exit the loop if saved successfully
    _try += 1

if _try == max_attempts:
    print("Exceeded maximum attempts. Program exiting.")
