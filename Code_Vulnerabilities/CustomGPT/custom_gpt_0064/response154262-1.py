
def Help():
    while True:
        string = input('What option do you choose: ')
        print('\n')

        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        else:
            print('The options available are: \n')
            for i in andHelp:
                print(i)
            print('Type Q to Quit \n')
            if string == 'Q':
                break

# Example usage
# Define the Manifest and Intent functions, and the andHelp list before calling Help()
def Manifest():
    return "Manifest Function Executed"

def Intent():
    return "Intent Function Executed"

andHelp = ['Manifest', 'Intent']

Help()
