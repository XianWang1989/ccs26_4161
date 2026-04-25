
def enterPass():
    for attempt in range(3):
        x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
        if x.isalnum():
            print("Saved")
            return  # Exit function upon successful input
        else:
            print("Try again")
    print("Exceeded attempts, quitting.")  # Indicate failure after 3 attempts
    return

# Calling the enterPass function
enterPass()
