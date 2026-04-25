
def enterPass():
    x = input("Enter password (Alpha or Alphanumeric, 'No_Space'): ")
    return x.isalnum()

def main():
    _try = 1
    while _try <= 3:
        if enterPass():
            print("Saved")
            break  # Exit loop on successful entry
        else:
            print("Try again")
            _try += 1

    if _try > 3:
        print("Exceeded maximum attempts. Program will quit.")

if __name__ == "__main__":
    main()
