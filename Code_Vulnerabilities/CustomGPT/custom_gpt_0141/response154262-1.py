
def Help(string):
    while True:
        # Check for the main options first
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
                # Assign the new input to 'string' to continue the loop
                string = x 

# Assuming Manifest() and Intent() are defined elsewhere,
# and andHelp is a list of options you want to display.
