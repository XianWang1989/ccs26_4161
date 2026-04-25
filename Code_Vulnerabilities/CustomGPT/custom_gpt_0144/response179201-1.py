def enterPass():
    x = raw_input("Enter password (Alpha or Alphanumeric, no spaces): ")
    if x.isalnum():
        print("Saved")
        return True
    else:
        print("Try again")
        return False

# Main loop
attempts = 1
while attempts <= 3:
    if enterPass():
        break
    attempts += 1
