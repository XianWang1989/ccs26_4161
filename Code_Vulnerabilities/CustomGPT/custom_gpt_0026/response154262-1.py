
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # Exit with call to Manifest()
        elif string == 'Intent':
            return Intent()    # Exit with call to Intent()
        else:
            print('The options available are: ')
            for i in andHelp:
                print(i)
            print('Type Q to Quit ')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break  # Exit the loop
            else:
                string = x  # Update string to the new choice

# Example usage
andHelp = ['Intent', 'Manifest']
def Manifest():
    return "You chose Manifest."

def Intent():
    return "You chose Intent."
