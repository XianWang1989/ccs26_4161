
def enterPass():
    for attempt in range(3):
        x = input("Enter password (alpha or alphanumeric, 'No_Space'): ")
        if x.isalnum():
            print("Saved")
            return  # Exit the function
        else:
            print("Try again")
    print("Exceeded maximum attempts.")

enterPass()
