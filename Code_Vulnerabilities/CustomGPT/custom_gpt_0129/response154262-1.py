
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
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
                # Update the string to reflect the new input
                string = x

# Sample usage (assuming Manifest and Intent functions are defined)
andHelp = ['Manifest', 'Intent']
Help('')  # Start the function with an empty string or other initial value
