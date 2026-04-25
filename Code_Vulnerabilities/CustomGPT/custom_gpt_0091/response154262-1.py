
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # Call the Manifest function
        elif string == 'Intent':
            return Intent()  # Call the Intent function
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
                string = x  # Set string to the new input to continue the loop

# Example usage:
andHelp = ['Intent', 'Manifest']  # Define possible options for the help
