
def enterPass():
    while True:
        x = input("Enter password (Alpha or Alphanumeric! 'No Space'): ")
        if x.isalnum():
            print("Saved")
            return True  # Indicates success
        else:
            print("Try again")

_try = 1
while _try <= 3:
    if enterPass():  # Check for success
        break
    _try += 1

if _try > 3:
    print("Exceeded maximum attempts.")
