
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # Assuming Manifest() is defined elsewhere
        elif string == 'Intent':
            return Intent()  # Assuming Intent() is defined elsewhere
        else:
            print('The options available are: \n')
            for i in andHelp:  # Assuming andHelp is defined
                print(i)
            print('Type Q to Quit \n')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break
            else:
                Help(x)  # Call Help function with the new input

# Example usage
andHelp = ['Intent', 'Manifest']  # Sample options
def Manifest():
    return "Manifest function called"

def Intent():
    return "Intent function called"

# Start the Help function
Help("Choose an option")
