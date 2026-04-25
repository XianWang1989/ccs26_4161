
def enterPass():
    for _try in range(1, 4):  # Allow up to 3 attempts
        x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
        if x.isalnum():
            print("Saved")
            return  # Exit the function upon success
        else:
            print("Try again")
    print("Exceeded maximum attempts. Please try again later.")

# Call the function
enterPass()
