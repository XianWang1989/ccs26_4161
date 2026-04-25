
def enterPass():
    while True:
        x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
        if x.isalnum():
            print("Saved")
            return True  # Successfully saved
        else:
            print("Try again")

# Main loop
tries = 0
max_tries = 3
while tries < max_tries:
    if enterPass():  # If a valid password is entered, exit loop
        break
    tries += 1

if tries == max_tries:
    print("Exceeded maximum attempts.")
