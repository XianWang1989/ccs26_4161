
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # Assuming Manifest is defined
        elif string == 'Intent':
            return Intent()    # Assuming Intent is defined
        else:
            print('The options available are: \n')
            for i in andHelp:  # Ensure 'andHelp' is defined somewhere in your code
                print(i)
            print('Type Q to Quit \n')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break
            else:
                # Instead of calling Help recursively, just assign the new value
                string = x  # Update the input for the next iteration
