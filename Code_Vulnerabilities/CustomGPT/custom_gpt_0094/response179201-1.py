
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    return x.isalnum()

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    if enterPass():
        print("Saved")
        break
    else:
        print("Try again")
        attempts += 1
else:
    print("Maximum attempts reached. Exiting.")
