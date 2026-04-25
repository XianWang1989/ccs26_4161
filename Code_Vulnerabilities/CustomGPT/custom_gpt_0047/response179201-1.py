
def enter_pass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Indicate successful input
    else:
        print("Try again")
        return False  # Indicate failure

try_count = 0
while try_count < 3:
    if enter_pass():
        break  # Exit the loop if the password is valid
    try_count += 1

if try_count == 3:
    print("Exceeded maximum attempts.")
