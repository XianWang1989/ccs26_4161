
def Help(string):
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
                # Update the string variable and continue the loop
                string = x

# Example to test Help function
andHelp = ['Intent', 'Manifest']
Help('Invalid')  # Start with an invalid option to demonstrate looping
