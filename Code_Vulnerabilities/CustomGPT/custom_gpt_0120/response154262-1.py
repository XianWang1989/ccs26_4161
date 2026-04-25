
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # Assumes Manifest() is defined
        elif string == 'Intent':
            return Intent()  # Assumes Intent() is defined
        else:
            print('The options available are: \n')
            for i in andHelp:  # Assumes andHelp is a predefined list
                print(i)
            print('Type Q to Quit \n')
            x = input('What option do you choose: ')
            print('\n')
            if x == 'Q':
                break
            else:
                # Update string with the new input
                string = x  # Set string to the new choice

# Example invocation
andHelp = ['Intent', 'Manifest']
# Call Help with an empty or initial string
Help('')
