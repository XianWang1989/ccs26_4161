
def Help():
    while True:
        x = input('What option do you choose (Type Q to Quit): ')
        print('\n')

        if x == 'Manifest':
            return Manifest()  # Assuming Manifest is defined elsewhere
        elif x == 'Intent':
            return Intent()  # Assuming Intent is defined elsewhere
        elif x.upper() == 'Q':
            break
        else:
            print('The options available are:')
            for i in andHelp:  # Assuming andHelp is defined elsewhere
                print(i)
            print()  # For better formatting

# Example of how Manifest and Intent might be defined
def Manifest():
    print("You selected Manifest.")

def Intent():
    print("You selected Intent.")

# Example options
andHelp = ['Manifest', 'Intent']

# Call the Help function
Help()
