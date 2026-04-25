
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # Ensure this function is defined elsewhere
        elif string == 'Intent':
            return Intent()  # Ensure this function is defined elsewhere
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break
            else:
                string = x  # Update the string to the user's input

# Usage example
andHelp = ["Intent", "Manifest"]  # Sample options
Help("default")  # Call Help with an initial value
