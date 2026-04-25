
def enter_pass():
    x = input("Enter password (Alpha or Alphanumeric! 'No_Space'): ")
    return x.isalnum()

def main():
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        if enter_pass():
            print("Saved")
            break
        else:
            print("Try again")
            attempts += 1

    if attempts == max_attempts:
        print("Max attempts reached. Exiting.")

if __name__ == "__main__":
    main()
