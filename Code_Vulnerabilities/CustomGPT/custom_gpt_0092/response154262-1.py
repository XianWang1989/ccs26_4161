
def Help():
    while True:
        string = input("What option do you choose (Manifest/Intent/Q to Quit): ")
        print('\n')

        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        elif string.upper() == 'Q':
            break
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')

# Example usage
# Define the Manifest and Intent functions
def Manifest():
    print("You chose Manifest.")

def Intent():
    print("You chose Intent.")

# List of helper options
andHelp = ['Intent', 'Manifest']
