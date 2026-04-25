
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # Call Manifest function
        elif string == 'Intent':
            return Intent()  # Call Intent function
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)  # Display help options
            print('Type Q to Quit \n')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break
            else:
                string = x  # Update the string to the new input
