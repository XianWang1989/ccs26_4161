
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
                # Update the string with the new input
                string = x

# Example function stubs for testing
def Manifest():
    return "You've chosen Manifest!"

def Intent():
    return "You've chosen Intent!"

# Example list for valid options
andHelp = ['Intent', 'Manifest']

# Starting the function
Help(input('What option do you choose: '))
