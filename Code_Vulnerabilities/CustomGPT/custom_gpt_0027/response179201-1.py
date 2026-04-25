
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True  # Return True if the password is valid
    else:
        print("Try again")
        return False  # Return False if the password is invalid

attempts = 3
while attempts > 0:
    if enterPass():  # If enterPass returns True, exit the loop
        break
    attempts -= 1
    if attempts == 0:
        print("Exceeded maximum attempts. Program quitting.")
