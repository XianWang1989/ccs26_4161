
def enterPass():
    while True:
        x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
        if x.isalnum():
            print("Saved")
            return True  # Exit when password is accepted
        else:
            print("Try again")
            return False  # Password not accepted

def main():
    _try = 0
    while _try < 3:
        if enterPass():  # Call the function and check for success
            break  # Exit the loop if the password is saved
        _try += 1

    if _try == 3:
        print("Exceeded maximum attempts. Program quitting.")

# Run the main function
main()
