
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # Assuming Manifest is defined elsewhere
        elif string == 'Intent':
            return Intent()     # Assuming Intent is defined elsewhere
        else:
            print('The options available are: \n')
            for i in andHelp:   # Assuming andHelp is defined elsewhere
                print(i)
            print('Type Q to Quit \n')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break
            else:
                # Instead of calling Help again, just set the string to x.
                string = x

# Example usage:
andHelp = ['Intent', 'Manifest']
def Manifest():
    return "You selected Manifest!"

def Intent():
    return "You selected Intent!"

# Start the help function
Help(None)
