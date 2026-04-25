
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # Call Manifest function
        elif string == 'Intent':
            return Intent()  # Call Intent function
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')
            # Take input from the user
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break
            else:
                # Update string for the next iteration of the loop.
                string = x

# Example functions
def Manifest():
    print("You selected Manifest!")
    # Additional logic here
    return

def Intent():
    print("You selected Intent!")
    # Additional logic here
    return

# Sample list for available help options
andHelp = ['Intent', 'Manifest']

# Start the help system
Help("initial")
