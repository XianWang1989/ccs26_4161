
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    return x.isalnum()

_attempts = 1
max_attempts = 3

while _attempts <= max_attempts:
    if enterPass():
        print("Saved")
        break
    else:
        print("Try again")
        _attempts += 1

if _attempts > max_attempts:
    print("Exceeded maximum attempts.")
