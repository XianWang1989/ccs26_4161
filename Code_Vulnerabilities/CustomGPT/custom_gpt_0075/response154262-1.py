
def Help():
    while True:
        x = input("What option do you choose (Manifest, Intent, or Q to Quit): ")
        print("\n")
        if x == 'Manifest':
            return Manifest()  # Assuming Manifest() is defined
        elif x == 'Intent':
            return Intent()     # Assuming Intent() is defined
        elif x == 'Q':
            print("Exiting...")
            break
        else:
            print("The options available are: \n")
            print("1. Manifest")
            print("2. Intent")
            print("Type Q to Quit \n")
