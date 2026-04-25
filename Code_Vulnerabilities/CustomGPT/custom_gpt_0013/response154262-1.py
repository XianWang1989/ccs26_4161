
def Help():
    while True:
        string = input('Enter "Manifest" or "Intent", or "Q" to Quit: ')
        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        elif string == 'Q':
            break
        else:
            print('The options available are: \n')
            for option in andHelp:
                print(option)
            print('Type Q to Quit \n')

# Example usage
andHelp = ['Manifest', 'Intent']
def Manifest():
    return "You selected Manifest!"

def Intent():
    return "You selected Intent!"

# Start the help function
Help()
