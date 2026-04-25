
def Help():
    while True:
        string = input('What option do you choose: ')
        print('\n')
        if string == 'Manifest':
            return Manifest()  # Call the Manifest function
        elif string == 'Intent':
            return Intent()  # Call the Intent function
        elif string == 'Q':
            print('Exiting the help menu.')
            break  # Exit the loop if user chooses to quit
        else:
            print('The options available are: \n')
            for i in andHelp:  # Assuming andHelp is a predefined list
                print(i)
            print('\nType Q to Quit \n')

# Example definitions for Manifest and Intent functions
def Manifest():
    print("Manifest chosen.")
    # Your Manifest code here

def Intent():
    print("Intent chosen.")
    # Your Intent code here

# Example usage
andHelp = ['Manifest', 'Intent']  # Define available options
Help()
