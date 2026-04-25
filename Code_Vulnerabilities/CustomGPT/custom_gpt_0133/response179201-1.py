
def enterPass():
    x = input("Enter password (Alphanumeric, 'No Space'): ")
    if x.isalnum():
        print("Saved")
        return True
    else:
        print("Try again")
        return False

_try = 1
while _try <= 3:
    if enterPass():  # If enterPass returns True, break the loop
        break
    _try += 1

if _try > 3:
    print("Exceeded maximum attempts.")
