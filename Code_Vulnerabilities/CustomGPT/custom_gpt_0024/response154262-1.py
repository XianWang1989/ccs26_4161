
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        else:
            print('The options available are: \n')
            for i in andHelp:  # Assuming andHelp is defined elsewhere
                print(i)
            print('Type Q to Quit \n')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break
            else:
                Help(x)  # Remove this line to avoid recursion

# Example usage of the Help function:
andHelp = ['Manifest', 'Intent']

def Manifest():
    print("Manifest selected")

def Intent():
    print("Intent selected")

# Start the function
Help(input('What option do you choose: '))
