
def enterPass():
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")

        if x.isalnum():
            print("Saved")
            return  # Exit the function if the input is valid
        else:
            print("Try again")
            attempts += 1

    print("Exceeded maximum attempts. Exiting.")

# Call the function
enterPass()
