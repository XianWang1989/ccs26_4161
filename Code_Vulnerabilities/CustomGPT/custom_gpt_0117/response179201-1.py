
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, No Spaces): ")
    return x.isalnum()

try_count = 1
max_tries = 3

while try_count <= max_tries:
    if enterPass():
        print("Saved")
        break
    else:
        print("Try again")
        try_count += 1
else:
    print("Maximum attempts reached. Exiting.")
