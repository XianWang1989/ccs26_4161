
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()
        elif string == 'Intent':
            return Intent()
        else:
            print('The options available are:')
            for i in andHelp:
                print(i)
            print('Type Q to Quit')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break
            else:
                string = x  # Update the string with the new choice

# Example usage (assuming Manifest and Intent are defined)
def Manifest():
    print("Manifest function called.")

def Intent():
    print("Intent function called.")

andHelp = ['Manifest', 'Intent']

# Call the help function
Help('Start')
