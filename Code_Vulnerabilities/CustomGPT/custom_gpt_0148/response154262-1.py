
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # Call Manifest function and return result
        elif string == 'Intent':
            return Intent()  # Call Intent function and return result
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
                string = x  # Update the string to the new input

# Example functions for demonstration
def Manifest():
    return "You selected Manifest."

def Intent():
    return "You selected Intent."

andHelp = ['Intent', 'Manifest']

# Initial call to the Help function
Help("start")
