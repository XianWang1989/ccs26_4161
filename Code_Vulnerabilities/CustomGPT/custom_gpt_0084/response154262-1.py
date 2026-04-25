
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        else:
            print('The options available are: \n')
            for i in andHelp:  # Assuming andHelp is defined
                print(i)
            print('Type Q to Quit \n')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break
            else:
                Help(x)  # This should not call Help again; change logic here

# Here's an alternative approach to keep track of user input:
def Help():
    while True:
        x = input('Choose an option (Manifest/Intent) or type Q to Quit: ')
        if x == 'Manifest':
            return Manifest()
        elif x == 'Intent':
            return Intent()
        elif x == 'Q':
            break
        else:
            print('Invalid option, please try again.\n')

# Replace Manifest and Intent with the actual implementations.
