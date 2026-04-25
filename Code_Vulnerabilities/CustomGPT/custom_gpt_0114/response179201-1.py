
def enterPass():
    for _ in range(3):  # Allow 3 attempts
        x = input("Enter password (Alpha or Alphanumeric! 'No_Space'):")
        if x.isalnum():
            print("Saved")
            return  # Exit the function and loop on success
        else:
            print("Try again")
    print("Exceeded maximum attempts.")

# Call the function
enterPass()
