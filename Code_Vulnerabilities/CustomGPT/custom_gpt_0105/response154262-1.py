
def Help(string):
    while True:
        if string == 'Manifest':
            return Manifest()  # This exits the function
        elif string == 'Intent':
            return Intent()  # This exits the function
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
                string = x  # Update the variable instead of calling Help recursively

# Example usage
andHelp = ['Intent', 'Manifest']  # Example list
