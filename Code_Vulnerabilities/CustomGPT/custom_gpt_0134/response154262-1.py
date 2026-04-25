
def help_options(string):
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
                # Update string for the next iteration
                string = x

# Example usage
andHelp = ['Manifest', 'Intent']
def Manifest():
    return "Manifest called"

def Intent():
    return "Intent called"

# Call the help_options function to start the interaction
help_options(input('Type "Manifest" or "Intent": '))
