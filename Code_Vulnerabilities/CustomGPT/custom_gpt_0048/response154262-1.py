
def Help():
    while True:
        print('The options available are: \n')
        for i in andHelp:
            print(i)
        print('Type Q to Quit \n')

        x = input('What option do you choose: ')
        print('\n')

        if x == 'Q':
            break
        elif x == 'Manifest':
            return Manifest()
        elif x == 'Intent':
            return Intent()
        else:
            print("Invalid option. Please choose again.\n")

# Example of andHelp list
andHelp = ['Intent', 'Manifest']

# Dummy functions for demonstration
def Manifest():
    return "Manifest function executed."

def Intent():
    return "Intent function executed."

# Call the Help function
Help()
