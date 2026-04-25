
def enterPass():
    while True:  # Keep prompting until a valid password is entered or tries exhaust
        x = raw_input("Enter password Alpha or Alphanumeric! 'No_Space': ")
        if x.isalnum():
            print("Saved")
            return True  # Return True if the password is valid
        else:
            print("Try again")

# Main loop for attempts
_try = 1
while _try <= 3:
    if enterPass():  # If valid password is entered
        break       # Exit the loop if the password was saved
    _try += 1

if _try > 3:
    print("Maximum attempts reached. Exiting.")
