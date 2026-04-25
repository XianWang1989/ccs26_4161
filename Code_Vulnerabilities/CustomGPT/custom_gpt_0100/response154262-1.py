
def Help():
    while True:
        string = input('What option do you choose: ')
        print('\n')

        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        elif string == 'Q':
            break
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')

# Example usage:
andHelp = ['Intent', 'Manifest']
def Manifest():
    return "You called Manifest!"

def Intent():
    return "You called Intent!"

# Start the Help function
Help()
