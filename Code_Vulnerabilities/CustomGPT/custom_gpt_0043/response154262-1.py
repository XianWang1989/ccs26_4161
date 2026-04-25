
def Help():
    while True:
        x = input("Type 'Manifest' for Manifest, 'Intent' for Intent, or 'Q' to Quit: ")
        print('\n')

        if x == 'Manifest':
            return Manifest()  # Replace with your actual function for Manifest
        elif x == 'Intent':
            return Intent()  # Replace with your actual function for Intent
        elif x == 'Q':
            print("Quitting the Help menu.")
            break
        else:
            print('The options available are: \n- Manifest\n- Intent\n')
            print('Type Q to Quit \n')

# Example Manifest and Intent function for demonstration
def Manifest():
    print("Manifest function executed.")

def Intent():
    print("Intent function executed.")

# Call Help to start the program
Help()
