
def Help():
    while True:
        # Display options to the user
        print('The options available are: \n')
        for i in andHelp:
            print(i)
        print('Type Q to Quit \n')

        # Get user choice
        x = input('What option do you choose: ')
        print('\n')

        # Handle user input
        if x == 'Q':
            break
        elif x == 'Manifest':
            return Manifest()  # Assuming Manifest is a defined function
        elif x == 'Intent':
            return Intent()     # Assuming Intent is a defined function
        else:
            print("Invalid option, please try again.")

# Example list to hold help options
andHelp = ['Manifest', 'Intent']

# Example function definitions
def Manifest():
    return "Manifest function executed."

def Intent():
    return "Intent function executed."

# Run the help function
Help()
