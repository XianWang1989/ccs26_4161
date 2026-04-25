
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    if x.isalnum():
        print("Saved")
        return True
    else:
        print("Try again")
        return False

def main():
    _try = 1
    while _try <= 3:
        if enterPass():  # Calls enterPass and checks the result
            break  # Exit loop if valid password is entered
        _try += 1

if __name__ == "__main__":
    main()
