
def Help():
    while True:
        string = input('What option do you choose: ')
        print('\n')
        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        elif string == 'Q':
            print("Quitting the Help menu.")
            break
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')

# Example functions for Manifest and Intent
def Manifest():
    print("Manifest function executed.")
    # Add actual implementation here

def Intent():
    print("Intent function executed.")
    # Add actual implementation here

# Example array for available options
andHelp = ['Manifest', 'Intent']

# Call the Help function to initiate
Help()
