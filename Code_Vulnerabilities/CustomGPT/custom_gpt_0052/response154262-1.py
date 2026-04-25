
def Help():
    while True:
        string = input('What option do you choose (Manifest/Intent/Q to Quit): ')
        print('\n')

        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        elif string == 'Q':
            break
        else:
            print('The options available are:')
            print('Manifest')
            print('Intent')
            print('Type Q to Quit')
            print('\n')

# Example implementations for Manifest and Intent functions
def Manifest():
    print("Manifest selected.")
    # Your Manifest code here

def Intent():
    print("Intent selected.")
    # Your Intent code here

# Call the Help function
Help()
